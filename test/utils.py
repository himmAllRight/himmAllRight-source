from os import listdir, path
import re


def get_file_paths(src, extension=None):
    """Collects the paths of all files of a directory"""
    file_list = []
    root_path = path.expanduser(src)
    for file in listdir(root_path):
        # If extension provided, check file has that extension
        if extension:
            if file.endswith(extension):
                file_list.append(path.join(root_path, file))
        # Otherwise, add everything
        else:
            file_list.append(path.join(root_path, file))
    return file_list


def get_file_names(src, extension=None):
    """Collects the names of all files of a directory"""
    file_list = []
    root_path = path.expanduser(src)
    for file in listdir(root_path):
        # If extension provided, check file has that extension
        if extension:
            if file.endswith(extension):
                file_list.append(file)
        # Otherwise, add everything
        else:
            file_list.append(file)
    return file_list


def get_file_content(file_list):
    """Grabs all the content from a list of file paths."""
    content_all_files = {}
    for file in file_list:
        f = open(file, "r")
        file_content = f.read()
        content_all_files[path.basename(file)] = file_content
    return content_all_files


def get_md_links(content_list, regex="\[.*\]\('(.*)'\)"):
    """Parses the list of content strings, and pulls out the url of any links."""
    p = re.compile(regex)
    all_links = []
    for file in content_list:
        content = content_list[file]
        match_iter = p.finditer(content)
        for match in match_iter:
            all_links.append((file, match.group(1)))
    return all_links
