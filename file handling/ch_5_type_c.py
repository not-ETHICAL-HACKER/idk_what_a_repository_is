def consecutive_spaces(file_name: str) -> None:
    """Reads a file and makes an identical file with all consecutive spaces reduced to a single space."""
    new_file_name = file_name.split(
        ".")[0] + "_updated." + file_name.split(".")[1]
    with open(file_name, 'r') as f:
        content = f.read()
        c = f.seek()
    updated = " ".join(content.split())

    with open(new_file_name, 'w') as f:
        f.write(updated)


def Event_dat_files(file_name: str, Event: str) -> None:
    """Reads a .dat file and makes a new .dat file with only the lines that contain the specified event."""
    ...


consecutive_spaces("q1.txt")
