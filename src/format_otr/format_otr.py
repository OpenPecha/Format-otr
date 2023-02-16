from pathlib import Path


def add_breaks_on_timestamps(text):
    """_summary_

    Args:
        text (_type_): _description_

    Returns:
        _type_: _description_
    """
    return text.replace("<span", "<p><br /></p> <span")


def remove_all_breaks(text):
    """_summary_

    Args:
        text (_type_): _description_

    Returns:
        _type_: _description_
    """
    return text.replace("<p><br /></p>", " ")


def get_format_otr(file_path_to_otr):
    otr_file_content = Path(file_path_to_otr).read_text("utf8")
    no_breaks_otr_content = remove_all_breaks(otr_file_content)
    format_otr = add_breaks_on_timestamps(no_breaks_otr_content)
    return format_otr.replace("\xa0", " ")
