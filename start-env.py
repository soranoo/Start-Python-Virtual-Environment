import os
import time
import sys

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__))) # get current directory

env_name = "env"
create_requirementstxt_cmd = "pip.exe freeze -l > requirements.txt"
start_env_cmd = f"cmd /k \"{os.path.join(os.getcwd(), env_name, 'Scripts', 'activate')}\""
create_env_cmd = f"py -m venv env"
install_requirements_cmd = f"pip install -r requirements.txt"

def is_env_exist(env_name):
	return os.path.isdir(os.path.join(os.getcwd(), env_name, 'Scripts'))

def load_env(extra_cmds = []):
	if is_env_exist(env_name):
		if (len(extra_cmds) > 0):
			for cmd in extra_cmds:
				os.system(cmd)
		os.system(start_env_cmd)
	else:
		print("No virtual environment found.")
		# ask the user create a new venv or not
		q1 = input("Do you want to create a new virtual environment? [y/n] ")
		q2 = False
		# if requirements.txt exists, ask the user if he wants to install the requirements
		if os.path.isfile(os.path.join(__location__, 'requirements.txt')):
			q2 = input("\n\"requirements.txt\" had been found.\nDo you want to install the requirements? [y/n] ")
			if q2.lower() == "y":
				q2 = True
		if q1.lower() == "y":
			print("\nCreating virtual environment...")
			print("(Virtual environment will start automatically after everything is done.)")
			os.system(create_env_cmd)
			if (q2 is True):
				extra_cmds.append(f"{install_requirements_cmd} --target={os.path.join(os.getcwd(), env_name, 'Lib', 'site-packages')}")
			if (len(extra_cmds) > 0):
				for cmd in extra_cmds:
					os.system(cmd)
			os.system(start_env_cmd)
		else:
			print("The program will shut down after 10s...")
			time.sleep(10)
			exit()

if __name__ == "__main__":
	if (len(sys.argv) > 1 and sys.argv[1] == "ctxt"):
		if (not is_env_exist("env")):
			print("No virtual environment found.")
			print("Are you still want to create a \"requirements.txt\" that containing all the dependencies?")
			q = input("[y/n] ")
			if (q.lower() == "y"):
				os.system(create_requirementstxt_cmd)
				print("Requirements.txt has been created.")
		else:
			print("Requirements.txt has been created.")
			load_env([f"{os.path.join(__location__, env_name, 'Scripts', 'pip.exe')} freeze -l > \"{os.path.join(__location__, 'requirements.txt')}\""])
	else:
		load_env()