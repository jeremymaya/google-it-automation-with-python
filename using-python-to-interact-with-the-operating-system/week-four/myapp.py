import os
import subprocess

# The copy method creates a new dictionary that can be changed as needed without modifying the original environment
my_env = os.environ.copy()

# The path variable indicates where the operating system will look for the executable programs
# Joins /opt/myapp and the old value of the path variable to the path separator
my_env["PATH"] = os.pathsep.join(["/opt/myapp/", my_env["PATH"]])

# Calls the myapp command, setting the end parameter to the new environment
result = subprocess.run(["myapp"], env=my_env)