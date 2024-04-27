import argparse
import glob
import shutil
import os

parser = argparse.ArgumentParser()
parser.add_argument("--input", default = ".", required = True)
parser.add_argument("--output", default = ".", required = True)
parser.add_argument("--cmd", required = False)
args = parser.parse_args()

for includePath in glob.glob("**/include", root_dir=args.input, recursive = True):
	shutil.copytree(os.path.join(args.input, includePath), os.path.join(args.output, "Include"),  dirs_exist_ok = True)
for suffix, outputDir in [("x86d", "x86/Debug"), ("x86", "x86/Release"), ("x64d", "x64/Debug"), ("x64", "x64/Release")]:
	for ext in ["dll", "lib", "so"]:
		for libPath in glob.glob("**/*" + suffix + "." + ext, root_dir=args.input, recursive = True):
			outputPath = os.path.join(args.output, outputDir)
			inputPath = os.path.join(args.input, libPath)
			if args.cmd is not None:
				os.system(args.cmd + " \"" + inputPath + "\"")
			if not os.path.exists(outputPath):
				os.makedirs(outputPath)
			shutil.copy(os.path.join(args.input, libPath), outputPath)