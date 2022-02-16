def lfs_url(repo, filename, branch='main'):
    '''
    Example
    ===========
    repo: 'SanstyleLab/plotly-datasets'
    branch: 'main'
    filename: 'gapminderDataFiveYear.csv'
    '''
    root = 'https://media.githubusercontent.com/media'
    return f'{root}/{repo}/{branch}/{filename}'