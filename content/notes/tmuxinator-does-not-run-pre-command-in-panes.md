



tmuxinator is a gread tool for the tmux. It gives a bunch of functionality which makes tmux more awesome. pre-window command of tmux will execute a given command after each window or pane is open. 
The below config will open three windows and one first one with 2 panes.
	
	
windows:
      - layout: main-vertical                                                     │~                                                                                                                
      panes:                                                                    │~                                                                                                                
        - vim                                                                   │~                                                                                                                
        - guard                                                                 │~                                                                                                                
  - server: bundle exec rails s                                                 │~                                                                                                                
  - logs: tail -f log/development.log



For me it was single window was working fine but when there is a pane in the window it wasn't working as expected. To resolve the issue just add the following line in ~/.tmux.conf file 

set -g base-index 1

set -g pane-base-index 1


