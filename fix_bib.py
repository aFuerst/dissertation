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
  # print(title)
  open_bracket = title.find('{')
  close_bracket = title.rfind('}')
  # print(open_bracket, close_bracket)
  just_title = title[open_bracket+1:close_bracket+1]
  just_title = just_title.replace("{", "")
  just_title = just_title.replace("}", "")
  just_title = '{' + '{' + just_title + '}' + '}'
  # print(just_title)
  before_title = title[:open_bracket]
  after_title = title[close_bracket+1:]
  # print(before_title, after_title)
  ret_title = before_title + just_title + after_title
  # print(ret_title)
  # exit()
  return ret_title

def end_of_part(line):
  return line.endswith("}\n") or line.endswith("},\n") or line.endswith(",\n")

def fix_reference(ref):
  ref_parts = []
  part = ""
  for line in ref:
    part += line
    if end_of_part(line):
      ref_parts.append(part)
      part = ""
  # print(ref_parts)
  # exit()
  ret_ref = []
  for part in ref_parts:
    if part.strip().startswith("title"):
      try:
        label, title = part.split('=')
      except Exception as e:
        print(f"'{part}'")
        raise e
      title = fix_title(title)
      part=f"{label}={title}"
    ret_ref.append(part)

  return ret_ref

def end_of_ref(line):
  return line == "}\n" or line == "}"

def fix_file(bib_file):
  with open(bib_file) as f:
    lines = f.readlines()

  refs = []
  i = 0
  while i < len(lines):
    line = lines[i]
    if line == "\n" or line.isspace():
      i += 1
      continue
    if line.startswith("#"):
      i += 1
      continue
    ref = []
    if line.startswith('@'):
      while not end_of_ref(line):
        ref.append(line)
        i += 1
        if i >= len(lines):
          break
        line = lines[i]
      ref.append(line)
    else:
      i += 1
      continue
    i += 1
    if len(ref) == 0:
      print("EMPTY REF")
      exit()
    try:
      ref = fix_reference(ref)
    except:
      pass
    ref = "".join(ref)
    refs.append(ref)

  print(len(refs))
  with open(bib_file, 'w') as f:
    for r in refs:
      f.write(r)
      f.write('\n')

all_bibs = find_bibs(".")
# fix_file(all_bibs[-1])
# exit()

for bib_file in all_bibs:
  print(bib_file)
  fix_file(bib_file)