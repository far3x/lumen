from ptap import visualizer
import os, json

#we test the json structure of the existing project here

#structure ALWAYS starts with files and its in alphabetical order since the algo I made was a bit different
#can't rly test the structure here since I'm updating the project way too much, so I just print the output and it should look like this in any os :
#this is the output when we ignore ".git", "ptap.egg-info" and "__pycache__" folders

"""
{
    "PTAP/": {
        "LICENSE": {},
        "README.md": {},
        "requirements.txt": {},
        "setup.py": {},
        ".git/": {},
        "ptap/": {
            "assembly.py": {},
            "file_reader.py": {},
            "main.py": {},
            "visualizer.py": {},
            "__init__.py": {}
        },
        "__pycache__/": {},
        "ptap.egg-info/": {},
        "tests/": {
            "assembly_test.py": {},
            "reader_test.py": {},
            "visualizer_test.py": {}
        }
    }
}
"""

#data print above
data = json.dumps( 
    visualizer.get_project_structure(
        root_path = os.getcwd(), 
        skipped_folders = [ #no need to specify the "/" element, and will show the directory but not the content
            ".git", 
            "__pycache__",
            "ptap.egg-info"
        ]
    ),
    indent = 4,
)

#print(data)

#output when nothing is ignored :

"""{
    "PTAP/": {
        "LICENSE": {},
        "README.md": {},
        "requirements.txt": {},
        "setup.py": {},
        ".git/": {
            "COMMIT_EDITMSG": {},
            "config": {},
            "description": {},
            "HEAD": {},
            "index": {},
            "hooks/": {
                "applypatch-msg.sample": {},
                "commit-msg.sample": {},
                "fsmonitor-watchman.sample": {},
                "post-update.sample": {},
                "pre-applypatch.sample": {},
                "pre-commit.sample": {},
                "pre-merge-commit.sample": {},
                "pre-push.sample": {},
                "pre-rebase.sample": {},
                "pre-receive.sample": {},
                "prepare-commit-msg.sample": {},
                "push-to-checkout.sample": {},
                "sendemail-validate.sample": {},
                "update.sample": {}
            },
            "info/": {
                "exclude": {}
            },
            "logs/": {
                "HEAD": {},
                "refs/": {
                    "heads/": {
                        "main": {}
                    },
                    "remotes/": {
                        "origin/": {
                            "main": {}
                        }
                    }
                }
            },
            "objects/": {
                "00/": {
                    "d40df93594a2de3792f27e5b1134f0bf386eee": {}
                },
                "03/": {
                    "42bc9300e947fc47c0e71eee9db77cfe122a57": {}
                },
                "0b/": {
                    "8daff7d84d9c463505dc28b659771bd369e1de": {}
                },
                "0f/": {
                    "92c9bf05c5bbdc1262d9903cb3d07980707336": {}
                },
                "11/": {
                    "f8b1783782f8046ea5de7e8b87dc5be756de1b": {}
                },
                "13/": {
                    "d2af98c4eeae950b38063b75481b28a034ff1f": {}
                },
                "18/": {
                    "b7b172a7fdd84fe47ac33d4dc0158372b918d3": {}
                },
                "22/": {
                    "827627c97972218ac8386f1ee53f9db353aca0": {}
                },
                "23/": {
                    "c27cba3f9bd071c6a6ab670c70d83ec9a608ac": {}
                },
                "24/": {
                    "d4c3fb6ec00f00ece33c1de87f1bddcff626b4": {}
                },
                "25/": {
                    "844ec4ac838f66516bc4cb5226f661f5a96b61": {}
                },
                "35/": {
                    "62d83c57be117ccd03586485294cad7c1fbf30": {}
                },
                "3a/": {
                    "f5318109c5eed523e19221f7e6d88eb9296311": {}
                },
                "42/": {
                    "cb70e0b7f083d0b81c3ed70af842441b254831": {}
                },
                "46/": {
                    "2b1bd9ef1452f36c674d1f85d5b29d9bdecd60": {}
                },
                "4d/": {
                    "584dc18827697f57b5370921c42b5fa7733c63": {}
                },
                "4f/": {
                    "1a87c9e767b440f7a67fc4a8f48e4b859017d1": {}
                },
                "50/": {
                    "4c8aa63fcc5aa091a2e2184b3e1a5f81777a62": {},
                    "5f86dee4a540a1570cb575a0352ed4c769e743": {}
                },
                "53/": {
                    "27bc88b8adbac0b9c6daffe07bc61963f44afc": {}
                },
                "5c/": {
                    "393a5c710e1b820015a471bbb7cc34e66bb522": {}
                },
                "5e/": {
                    "abdb61e08e74c8c343b5293091df6ba7e03a54": {}
                },
                "69/": {
                    "8e9a1edc6982b5b57fc7d31a0968c6323fcc71": {}
                },
                "74/": {
                    "fbb1ae9d0599265ad7b99ef7f8f4d69131c099": {}
                },
                "77/": {
                    "1bd9696f9d6b924be3e307fb38f4c175d34290": {}
                },
                "78/": {
                    "b5fa62c95229dce91a24868772b3580cc2becb": {}
                },
                "82/": {
                    "e0644cd7b56ed21a5cd3668b9b927b6095bcd9": {}
                },
                "87/": {
                    "816b327dc9b9b4f749e9ef2e59fddf6ff96e78": {},
                    "a376c5156653956093b472bc71fbf3f1408f7f": {},
                    "a67c73406b071f7782eaf4ba9bea95721d0d25": {}
                },
                "8b/": {
                    "137891791fe96927ad78e64b0aad7bded08bdc": {}
                },
                "98/": {
                    "afe9a222a963d87f778fc765841d13bed250b9": {}
                },
                "9e/": {
                    "005bd4a7372c8a958e7c3866f6f03575ece571": {},
                    "978156853c6167df5f2e4792de3b1be7fa8cad": {}
                },
                "a0/": {
                    "9809dcf17602e7db739b4aa2c6ed3e34d38766": {}
                },
                "a3/": {
                    "8a7629dfd1a6969d70e7103590b2a45f441890": {},
                    "a2191bdf00268fb155d3aaf7cd1399ec80ab09": {}
                },
                "a8/": {
                    "456cdabf77673e26e02c5507e39d21fc9a3aaa": {}
                },
                "a9/": {
                    "0a97a983f677c420779e8591547e8ecfdfc621": {}
                },
                "ae/": {
                    "3affdc1bd19ce0dd99782a938b1a28779c7efe": {}
                },
                "b2/": {
                    "86ebfbacf1f96609822dcaf299978e745f88d6": {},
                    "a6a13073973e2afdb892e5261b0186b4a98bb9": {}
                },
                "b5/": {
                    "633a910a9233132612dd0c1798b43ee5b26e38": {}
                },
                "b6/": {
                    "088a259285acd37202823d52351cdefe57f5e7": {}
                },
                "b8/": {
                    "3fcf0012422a629ceae82bfadbae699339ad6a": {},
                    "a4e93fb5dcb048c1cc7ac32e892234a9cb9bfb": {}
                },
                "b9/": {
                    "8217911955150fe2e6523696ee25914df28168": {}
                },
                "bf/": {
                    "0048ecddcd2347e0fe447718885699fe0b465e": {}
                },
                "c9/": {
                    "61ed357d46dc265255f8a04909efd15f46f447": {},
                    "6653161d0e214aa26500e5d70e582c5a7b97a9": {}
                },
                "ca/": {
                    "0de042a43b4fb93588a662e39773df84c5a846": {}
                },
                "d0/": {
                    "20a90a7cdcee2d060e8c789430f0dae19880e9": {}
                },
                "d4/": {
                    "f7edfabe750534280197efdd66003a4ecff704": {}
                },
                "d5/": {
                    "6560fa9a69442fbb363804a64d203559fc0572": {}
                },
                "dd/": {
                    "26402192aba33d7c12789e456ac177f719f1a8": {}
                },
                "e0/": {
                    "e2cc64830f21e0bdd999d8eccaa3d37d88ff78": {}
                },
                "e6/": {
                    "7f00ecc4e1b0a3b8b6fe6c362fd68a3d9f6fce": {},
                    "9de29bb2d1d6434b8b29ae775ad8c2e48c5391": {}
                },
                "e7/": {
                    "267aabecce91285f8bbefe5446daf0c99133a9": {}
                },
                "ef/": {
                    "347cf20dd2af55fcde71283add5112248ad2f9": {},
                    "df46c65d840ce1f53f7e013172a8f82ebb9603": {}
                },
                "f0/": {
                    "c4a84ba971fc82a66735890d9c66349430a78a": {}
                },
                "info/": {},
                "pack/": {}
            },
            "refs/": {
                "heads/": {
                    "main": {}
                },
                "remotes/": {
                    "origin/": {
                        "main": {}
                    }
                },
                "tags/": {}
            }
        },
        "ptap/": {
            "assembly.py": {},
            "file_reader.py": {},
            "main.py": {},
            "visualizer.py": {},
            "__init__.py": {},
            "__pycache__/": {
                "assembly.cpython-310.pyc": {},
                "file_reader.cpython-310.pyc": {},
                "visualizer.cpython-310.pyc": {},
                "__init__.cpython-310.pyc": {}
            }
        },
        "ptap.egg-info/": {
            "dependency_links.txt": {},
            "entry_points.txt": {},
            "PKG-INFO": {},
            "SOURCES.txt": {},
            "top_level.txt": {}
        },
        "tests/": {
            "assembly_test.py": {},
            "reader_test.py": {},
            "visualizer_test.py": {}
        }
    }
}"""

#data print above
data = json.dumps(
    visualizer.get_project_structure(
        root_path = os.getcwd(), 
        skipped_folders = [ 
            #no need to specify the "/" element, and will show the directory but not the content
        ]
    ),
    indent = 4,
)

#print(data)