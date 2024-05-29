import os, os.path

def find_bibs(path):
  found = []
  for search_pth in os.listdir(path):
      search_pth = os.path.join(path, search_pth)
      if os.path.isdir(search_pth):
        found += find_bibs(search_pth)
      elif os.path.isfile(search_pth) and search_pth.endswith(".bib"):
        found.append(search_pth)

  return found

def fix_title(title):
  return title

def fix_reference(ref):
  parts = ref.split('\n')
  i = 0
  while i < len(parts):
    part = parts[i]
    if part.strip().startswith("title"):
      label, title = part.split('=')
      title = title.strip()
      if not (title.startswith('{') and (title.endswith('},') or title.endswith('}'))):
        print(title)
        if '=' in parts[i+1]:
          title += parts[i+1]
          print("ADDED")
          print(title)
        else:
          print(part)
          print(f"'{title}'")
          print(ref)
          exit()

    i += 1
  return ref

def fix_file(bib_file):
  with open(bib_file) as f:
    lines = f.readlines()

  refs = []
  i = 0
  while i < len(lines):
    line = lines[i].strip("\n")
    if len(line) == 0 or line.isspace():
      # print(line)
      i += 1
      continue
    if line.startswith("#"):
      # print(line)
      i += 1
      continue
    ref = []
    # print(line)
    if line.startswith('@'):
      while line != "}":
        # print(line)
        ref.append(line) 
        i += 1
        line = lines[i].strip("\n")
      # print(line)
      ref.append(line)
    else:
      i += 1
      continue
    i += 1
    if len(ref) == 0:
      # print(bib_file)
      print("EMPTY REF")
      exit()
    ref = "\n".join(ref)
    ref = fix_reference(ref)
    refs.append(ref)

  print(len(refs))
  # print(refs[0:4])
  # exit()
  with open(bib_file, 'w') as f:
    for r in refs:
      f.write(r)
      f.write('\n')
      f.write('\n')

all_bibs = find_bibs(".")
# print(len(all_bibs))
# print(all_bibs)

# fix_file(all_bibs[-1])
# exit()

for bib_file in all_bibs:
  print(bib_file)
  fix_file(bib_file)