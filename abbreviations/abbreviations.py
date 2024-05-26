import subprocess

found_abbreviations = set()

args = ["grep --include '*.tex' -r -P '(?:\\b[A-Z]+[A-Zs]){1,}\\b' -o .."]
# args = ["grep --include '*.tex' --exclude='xstring' -r --invert-match '%' . | grep --invert-match 'command' |  grep -P '(?:\\b[A-Z]+[A-Zs]){1,}\\b'"]
print(args)
output = subprocess.run(args, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
if output.returncode != 0:
  print("ERROR")
  print(output.stdout)
  print(output.stderr)
  exit(output.returncode)

ignore = set()
with open("ignore") as f:
  for line in f.readlines():
    ignore.add(line.strip())

# print(output.stdout)
for line in output.stdout.split('\n'):
  # for line in lines:
  # print(line)
  if ':' in line:
    try:
      file, abbrev = line.split(':')
    except Exception as e:
      print(line)
      # raise e
      continue
    if abbrev[-1] == 's':
      abbrev = abbrev[:-1]
    if abbrev in ignore:
      continue
    if len(abbrev) > 1:
      found_abbreviations.add(abbrev)

# print(len(found_abbreviations))
existing_abbrevs = set()
abbrevs_write = []
with open("abbreviations.done") as f:
  for line in f.readlines():
    abbrevs_write.append(f"{line.strip()} \\\\\n")
    abbrev, *_ = line.split(':')
    existing_abbrevs.add(abbrev)
    # print(line)

abbrevs_write = sorted(abbrevs_write)
abbrevs_write.insert(0, "\\noindent\n")
# abbrevs_write.append("\n}")
with open("../abbreviations.tex", 'w') as f:
  f.writelines(abbrevs_write)

# print(existing_abbrevs)
with open("abbreviations.grep", "w") as f:
  for abbrev in found_abbreviations:
    if abbrev not in existing_abbrevs:
      f.write(f"{abbrev}\n")
