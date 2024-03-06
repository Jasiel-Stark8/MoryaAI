from graphviz import Digraph

def add_nodes(dot, path, node, is_root=False):
    for name, child in node.items():
        child_path = f"{path}/{name}" if path else name
        if child:  # it's a directory if it has children
            shape = 'box'
        else:  # it's a file if it has no children
            shape = 'ellipse'

        dot.node(child_path, name, shape=shape, style='filled', fillcolor='lightgrey' if child else 'white')

        if path:  # Avoid linking from the root ('')
            dot.edge(path, child_path)
        if child:  # Recursion to add child nodes
            add_nodes(dot, child_path, child)

tree = {
    ".": {
        "Developers_Notes.md": {},
        "LICENSE": {},
        "README.md": {},
        "client": {
            "file": {},
            "public": {
                "README.md": {},
                "env.d.ts": {},
                "index.html": {},
                "package-lock.json": {},
                "package.json": {},
                "postcss.config.js": {},
                "src": {
                    "App.vue": {},
                    "assets": {
                        "base.css": {},
                        "logo.svg": {},
                        "main.css": {}
                    },
                    "components": {
                        "DashboardPage.vue": {},
                        "GenerationPage.vue": {},
                        "ProfilePage.vue": {},
                        "SignIn.vue": {},
                        "SignUp.vue": {},
                        "__tests__": {
                            "HelloWorld.spec.ts": {}
                        },
                        "icons": {
                            "IconCommunity.vue": {},
                            "IconDocumentation.vue": {},
                            "IconEcosystem.vue": {},
                            "IconSupport.vue": {},
                            "IconTooling.vue": {}
                        }
                    },
                    "index.css": {},
                    "main.ts": {},
                    "router": {
                        "index.ts": {}
                    },
                    "stores": {
                        "counter.ts": {}
                    },
                    "test": {},
                    "views": {
                        "SideBar.vue": {}
                    }
                },
                "tailwind.config.js": {},
                "tsconfig.app.json": {},
                "tsconfig.json": {},
                "tsconfig.node.json": {},
                "tsconfig.vitest.json": {},
                "vite.config.ts": {},
                "vitest.config.ts": {}
            },
            "tes": {}
        },
        "server": {
            "app": {
                "__init__.py": {},
                "api": {
                    "__init__.py": {},
                    "v1": {
                        "core": {
                            "__init__.py": {},
                            "auth.py": {},
                            "generate.py": {},
                            "settings.py": {},
                            "subscribe.py": {},
                            "view_articles.py": {}
                        },
                        "llms": {
                            "GPT-2-conversation_dataset.json": {},
                            "__init__.py": {},
                            "distil.py": {},
                            "distilgpt2": {
                                "64.tflite": {},
                                "README.md": {},
                                "config.json": {},
                                "coreml": {
                                    "text-generation": {
                                        "float32_model.mlpackage": {
                                            "Data": {
                                                "com.apple.CoreML": {
                                                    "model.mlmodel": {},
                                                    "weights": {
                                                        "weight.bin": {}
                                                    }
                                                }
                                            },
                                            "Manifest.json": {}
                                        }
                                    }
                                },
                                "coreml_model.mlmodel": {},
                                "flax_model.msgpack": {},
                                "generation_config.json": {},
                                "generation_config_for_text_generation.json": {},
                                "merges.txt": {},
                                "model.safetensors": {},
                                "pytorch_model.bin": {},
                                "rust_model.ot": {},
                                "tf_model.h5": {},
                                "tokenizer.json": {},
                                "tokenizer_config.json": {},
                                "vocab.json": {}
                            },
                            "finetune.py": {},
                            "pat": {},
                            "post.py": {},
                            "train.py": {}
                        },
                        "routes": {
                            "__init__.py": {}
                        }
                    }
                },
                "database.py": {},
                "models": {
                    "__init__.py": {},
                    "articles.py": {},
                    "platforms.py": {},
                    "published_content.py": {},
                    "users.py": {},
                    "voice_drafts.py": {}
                }
            },
            "app.py": {},
            "requirements.txt": {},
            "tests": {
                "__init__.py": {},
                "test_auth.py": {}
            }
        }
    }
}

dot = Digraph(comment='Project Structure', format='png')
dot.attr(rankdir='LR', size='12,12')  # Left to Right layout, increase the size as needed
add_nodes(dot, '', tree, is_root=True)

# Render the dot file and open the image
output_path = '/mnt/data/project_structure_improved'
dot.render(output_path, view=False)

return output_path + '.png'
