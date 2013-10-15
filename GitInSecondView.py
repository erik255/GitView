import sublime, sublime_plugin

class GitInSecondViewCommand(sublime_plugin.WindowCommand):
	
	def run(self):
		gr=self.window.views_in_group(1)

		print ('open Windows={}'.format(len(gr)))
		#print ('Windows1={}'.format(gr[0].name()))

		found=False

		for v in gr:
			if '*git-status*' in v.name():
				found=True
				#print ('found a git status! ->we close it')			
				self.window.focus_view(v)
				self.window.run_command("close_file")
				if len(gr) is 1:
					#print ('as only view ! -> so we close it and the group')			
					self.window.run_command("focus_group", { "group": 0 })
					self.window.run_command("set_layout",{"cols": [0.0, 1.0],"rows": [0.0, 1.0],"cells": [[0, 0, 1, 1]]	})
									

		if found is False:
			#print ('found no git status! ->we open it')	
			self.window.run_command("set_layout",{"cols": [0.0, 0.65, 1.0],"rows": [0.0, 1.0],"cells": [[0, 0, 1, 1], [1, 0, 2, 1]]})
			self.window.run_command("focus_group", { "group": 1 })
			self.window.run_command("git_status")

		
	    	
	    	

