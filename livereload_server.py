from livereload import Server, shell


server = Server()
server.watch('.', shell('make html', cwd='.'))
server.serve(root='.')