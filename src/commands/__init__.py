from .build import Build

commands = {
    "build": {
        "description": "Build the site.",
        "callback": Build.run
    }
}
