"""
    EAL - Easy Addon Localisation

    Pytests for EAL

    @author DevonDF
    @website devon.computer
"""

import pytest
import eal
import os
import pathlib
import shutil

PATH = pathlib.Path(__file__).parent

def emulate_test_addon(addon):
    """
        Creates a new tempdir for the given addon template, and sets
            the current working path inside

        @params - String - Addon name to change to
    """
    src_path = PATH.joinpath("test_addons", addon)
    target_path = PATH.joinpath("tmp")
    shutil.copytree(src_path, target_path, dirs_exist_ok=True)
    os.chdir(target_path)
    eal.PATH = target_path.joinpath("eal.py")

class TestEAL:

    path = None

    @classmethod
    def setup_class(cls):
        path = emulate_test_addon("test_1")
        eal.input = lambda x: "y"
        eal.main()

    def test_create_folders(self):
        assert PATH.joinpath("tmp").joinpath("lua","eal_tmp").exists()
        assert PATH.joinpath("tmp").joinpath("lua","eal_tmp", "langs").exists()
    
    def test_create_files(self):
        assert PATH.joinpath("tmp").joinpath("lua","eal_tmp", "eal.lua").exists()
        for lang in eal.LANGUAGES:
            assert PATH.joinpath("tmp").joinpath("lua","eal_tmp", "langs", f"{lang}.lua").exists()
    
    def test_create_globals(self):
        with open(PATH.joinpath("tmp").joinpath("lua", "test_addon", "init.lua"), "r") as f:
            with open(PATH.joinpath("test_addons", "test_1", "lua", "test_addon", "init.lua"), "r") as o:
                assert 1 # TODO

    
    @classmethod
    def teardown_class(cls):
        shutil.rmtree(PATH.joinpath("tmp", "lua"))


