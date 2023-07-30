from pathlib import Path


__all__ = ['filerenamer']


def filerenamer(*, filename='', count_length=1, u_range=None, old_ext=None, new_ext=None, filepath='.'):
    path = Path(filepath)
    count = 0
    if new_ext is None:
        ext = old_ext
    else:
        ext = new_ext
    if old_ext is None:
        for i in path.iterdir():
            if i.is_file():
                old_name = _check_range(i.stem, u_range)
                i.rename(f'{path}/{old_name}{filename}{count + 1:0{count_length}}{i.suffix}')
                count += 1
    else:
        for i in path.iterdir():
            if i.is_file() and i.suffix == old_ext:
                old_name = _check_range(i.stem, u_range)
                i.rename(f'{path}/{old_name}{filename}{count + 1:0{count_length}}{ext}')
                count += 1


def _check_range(name, u_range):
    if u_range is not None:
        if len(name) < u_range[1]:
            if len(name) < u_range[0]:
                return 'ERROR'
            else:
                return f'{name[u_range[0]:len(name)]}'
        else:
            return f'{name[u_range[0]:u_range[1]]}'
    return ''


if __name__ == '__main__':
    filerenamer(filename='test', count_length=3, u_range=(2, 5), old_ext='.txt', new_ext='.jpg', filepath='../test')
