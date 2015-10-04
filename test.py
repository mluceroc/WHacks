import models

a = models.Location('42.360082', '-71.058880')
b = models.Location('42.525656', '-71.095289')

g = models.Graph(a, b)
print g.get_paths()
