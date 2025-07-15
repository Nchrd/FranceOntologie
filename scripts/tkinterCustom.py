import tkinter as tk
from tkinter import ttk

class AutocompleteCombobox(ttk.Frame):
    def __init__(self, master=None, values=None, **kwargs):
        super().__init__(master, **kwargs)
        self._completion_list = values or []
        
        # Entry styled like Combobox
        self.var = tk.StringVar()
        self.entry = ttk.Entry(self, textvariable=self.var)
        self.entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
        
        # Button to show/hide dropdown manually
        self.button = ttk.Button(self, text="▾", width=2, command=self._toggle_list)
        self.button.pack(side=tk.RIGHT)
        
        # Popup window for the dropdown
        self.listbox_window = None
        self.var.trace_add('write', self._on_change)
        self.entry.bind('<Down>', lambda e: self._open_list())
        self.entry.bind('<Up>',   lambda e: self._open_list())
        self.entry.bind('<Return>', lambda e: self._select_current())

    def set_completion_list(self, completion_list):
        self._completion_list = completion_list

    def _on_change(self, *args):
        # Update & reopen dropdown every time text changes
        if self.listbox_window:
            self._update_list()
        else:
            self._open_list()

    def _toggle_list(self):
        if self.listbox_window:
            self._close_list()
        else:
            self._open_list()

    def _open_list(self):
        if self.listbox_window:
            return
        # Create top-level just below the entry
        x = self.entry.winfo_rootx()
        y = self.entry.winfo_rooty() + self.entry.winfo_height()
        self.listbox_window = tk.Toplevel(self)
        self.listbox_window.wm_overrideredirect(True)
        self.listbox_window.wm_geometry(f"+{x}+{y}")
        
        self.listbox = tk.Listbox(self.listbox_window)
        self.listbox.pack(expand=True, fill=tk.BOTH)
        self.listbox.bind("<<ListboxSelect>>", lambda e: self._select_current())
        self.listbox.bind("<Escape>", lambda e: self._close_list())
        
        self._update_list()

    def _update_list(self):
        search = self.var.get().lower()
        matches = [w for w in self._completion_list if search in w.lower()] if search else list(self._completion_list)
        
        # repopulate
        self.listbox.delete(0, tk.END)
        for w in matches:
            self.listbox.insert(tk.END, w)
        if matches:
            # keep the dropdown visible
            self.listbox.selection_clear(0, tk.END)
            self.listbox.selection_set(0)

    def _select_current(self):
        if not self.listbox_window:
            return
        sel = self.listbox.curselection()
        if sel:
            value = self.listbox.get(sel[0])
            self.var.set(value)
            self.entry.icursor(tk.END)
        self._close_list()

    def _close_list(self):
        if self.listbox_window:
            self.listbox_window.destroy()
            self.listbox_window = None

    def get(self):
        return self.var.get()
