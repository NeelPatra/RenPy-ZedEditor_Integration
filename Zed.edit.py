import renpy.editor
import subprocess
import os

class Editor(renpy.editor.Editor):

    def begin(self, new_window=False, **kwargs):
        """
        Starts an editor transaction.
        If new_window is True, we tell Zed to open a new window.
        """
        self.arguments = []
        if new_window:
            # Zed uses '--new' or '-n' to force a new window
            self.arguments.append("--new")

    def open(self, filename, line=None, **kwargs):
        """
        Adds a file to the current transaction.
        Zed supports the 'file:line' syntax.
        """
        if line:
            # Format: filename:line
            target = f"{filename}:{line}"
        else:
            target = filename
            
        self.arguments.append(target)

    def end(self, **kwargs):
        """
        Ends the transaction and actually executes the Zed command.
        """
        # We call the 'zed' command with all collected file arguments
        try:
            # This assumes 'zed' is in system PATH
            subprocess.Popen(["zed"] + self.arguments)
        except Exception as e:
            renpy.log.write(f"Could not launch Zed: {e}")
            pass