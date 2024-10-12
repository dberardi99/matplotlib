ReadMe-issue-28268

1. What clear/cla should do?

These commands should:
- Remove all data-like content from the picture
- Keep the layout unchanged (thus axes position, twinning, etc. should stay)
- Reset the formatting? We could introduce a "cla(reset="reset")" like Matlab to do an "hard clear", thus clearing also the formatting. This is probably the most suitable choice.

IMHO, cla should only clear data (thus clearing the plot and resetting the axes bounds). Then, if I want to delete also the formatting (title/labels/lables color/lables position etc.) I
could run "cla(reset='reset')", which means a sort of hard reset of the axes.

2. Various commands:

ax0.dataLim -> It returns the values bounds (deafult: 0-1)
ax0.viewLim -> It returns the axis bounds (deafult: 0-1)
ax0.yaxis.label_position -> It says where the title is with "twinx" (default: right)
ax1.yaxis.label._text -> It prints the y axis label

3. What happens when the "cla" command is called?

	1. test.py
	2. _base.py
	3. axis.py
	4. text.py

4. ToDo:

- What does "_reset_visual_defaults" do? Check from line 157 in text.py
- Side effects related to the introduction of 'reset' property (check what happens in the "_init")
- Check if "clear" is called in other routines
- Investigate the other actions performed while calling "clear" (e.g., "self.label.set_color(mpl.rcParams['axes.labelcolor'])")

5. Coding guidelines:
- Pass "reset" property as *kwargs and then pop out its value by calling "kwargs.pop" (e.g., see line 1514 of file pyplot.py)

if 'reset' in kwargs and len(kwargs) == 1: # To check if the user is calling the "reset" property
	reset = kwargs.pop('reset')
	print(reset) # DEBUG
		if typeof(reset) is not bool:
			raise TypeError(
				"'reset' must be used a bool. It has been set to False")
			reset = False
	print(reset)

elif 'reset' in kwargs and len(kwargs) > 1: # The user has called "reset" and other properties (not possible right now)
	raise TypeError(
		"'clear' can accept only one argument")
	reset = kwargs.pop('reset')
		if typeof(reset) is not bool:
			raise TypeError(
				"'reset' must be used a bool. It has been set to False")
			reset = False # Default value for "reset" is False
	print(reset)
elif ('reset' is not in kwargs and len(kwargs) == 1):
	raise TypeError(
		"kwargs[0] property cannot be accepted")
	reset = False

elif len(kwargs) < 1:
	reset False

