from __future__ import with_statement
import hashlib
from os.path import join

from fabric.api import local, lcd, settings
from fabric.colors import green, yellow
from constants import CORE_REPO, ADDONS


class Generator(object):

    def __init__(self, config, dry_run=True):
        self.config = config
        self.dry_run = dry_run

    @property
    def config_hash(self):
        return self.get_hash_input(self.config)

    @property
    def tmp(self):
        return join('/', 'tmp')

    @property
    def build_dir(self):
        return join(self.tmp, self.config_hash)

    @property
    def build_branch(self):
        return "build/%s" % self.config_hash

    def get_hash_input(self, input):
        input['addons'] = set(input.get('addons', []))
        return hashlib.sha1('%s' % sorted(input.items())).hexdigest()

    def clean(self):
        """
        Remove temp dir if exists
        """
        local('rm -rf %s' % self.build_dir)

    def clone_core(self):
        """
        Clone the core template and put it in the tmp folder
        """
        self.clean()
        with lcd(self.tmp):
            local("git clone %s %s" % (CORE_REPO, self.config_hash))

    def merge_addon(self, addon):
        """
        Merges the addon branch
        """
        msg = "Merging %s" % addon.display
        local("git merge origin/%s -m '%s'" % (addon, msg))

    def commit(self):
        """
        Pushes the branch to origin
        """
        local("git push origin HEAD")

    def previously_built(self):
        """
        Checks if there's already a branch for the build
        """
        with settings(warn_only=True):
            response = local(
                "git rev-parse --verify origin/%s" % self.build_branch,
                capture=True)
        return response.succeeded

    def run(self):
        print(green("Building the core django template %s" % self.config_hash))
        self.clone_core()

        with lcd(self.build_dir):
            if self.previously_built():
                print(yellow("Build Branch already exists!"))
                print(green(self.build_branch))
                return

        print(green("Creating a new branch and merging addons"))
        with lcd(self.build_dir):
            local("git checkout -b %s" % self.build_branch)
            for addon in self.config['addons']:
                print(yellow("Installing %s" % addon.display))
                self.merge_addon(addon)

            if not self.dry_run:
                print(green("Pushing build to github"))
                self.commit()
            print(green(self.build_branch))


def generate():
    config = {
        'addons': [
            ADDONS.PIPELINE,
            ADDONS.JINJA2,
        ]
    }
    Generator(config, dry_run=True).run()
