def compare(old: dict, new: dict) -> list[str]:
    changes = []
    for k in old.keys() ^ new.keys(): changes.append(f'Key mismatch: {k}')
    return changes
