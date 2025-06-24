from livereload import Server, shell


server = Server()
server.watch(
    '*',
     shell('make html', cwd='simple_video_player')
     )
     
server.serve(root='.')