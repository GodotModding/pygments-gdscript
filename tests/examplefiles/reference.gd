# from https://docs.godotengine.org/en/stable/tutorials/scripting/gdscript/gdscript_basics.html
# stable = 4.4, modified to be a valid script

# Everything after "#" is a comment.
# A file is a class!

# (optional) icon to show in the editor dialogs:
@icon("res://path/to/optional/icon.svg")

# (optional) class definition:
class_name MyClass

# Inheritance:
extends BaseClass


# Member variables.
var a = 5
var s = "Hello"
var arr = [1, 2, 3]
var dict = {"key": "value", 2: 3}
var other_dict = {key = "value", other_key = 2}
var typed_var: int
var inferred_type := "String"

# Constants.
const ANSWER = 42
const THE_NAME = "Charly"

# Enums.
enum {UNIT_NEUTRAL, UNIT_ENEMY, UNIT_ALLY}
enum NamedEnum {THING_1, THING_2, ANOTHER_THING = -1}

# Built-in vector types.
var v2 = Vector2(1, 2)
var v3 = Vector3(1, 2, 3)

# Signals
signal some_signal

# Functions.
func some_function(param1, param2, param3):
	const local_const = 5

	if param1 < local_const:
		print(param1)
	elif param2 > 5:
		print(param2)
	else:
		print("Fail!")

	for i in range(20):
		print(i)

	while param2 != 0:
		param2 -= 1

	match param3:
		3:
			print("param3 is 3!")
		_:
			print("param3 is not 3!")

	var local_var = param1 + 3
	return local_var


# Functions override functions with the same name on the base/super class.
# If you still want to call them, use "super":
func something(p1, p2):
	super(p1, p2)


# It's also possible to call another function in the super class:
func other_something(p1, p2):
	super.something(p1, p2)


# Inner class
class Something:
	var a = 10


# Constructor
func _init():
	print("Constructed!")
	var lv = Something.new()
	print(lv.a)


func operators():
	var x
	var y

	(x) # Grouping
	x[1] # Subscription
	x.attribute # Attribute reference
	something(1, 2) # Function call
	await some_signal # Awaiting signals or coroutines

	x is Node # Type checking
	x is not Node

	x ** y # Power
	~x # Bitwise NOT
	+x -x # Identity / Negation

	x * y # Multiplication / Division / Remainder
	x / y
	x % y

	x + y # Addition (or Concatenation) / Subtraction
	x - y

	x << y # Bit shifting
	x >> y
	x & y # Bitwise AND
	x ^ y # Bitwise XOR
	x | y # Bitwise OR

	x == y # Comparison
	x != y
	x < y
	x > y
	x <= y
	x >= y

	x in y # Inclusion checking
	x not in y

	not x # Boolean NOT and its unrecommended alias
	!x

	x and y # Boolean AND and its unrecommended alias
	x && y

	x or y # Boolean OR and its unrecommended alias
	x || y

	"true_expr" if true else "false_expr" # Ternary if/else

	x as Node # Type casting

	x = y # Assignment
	x += y
	x -= y
	x *= y
	x /= y
	x **= y
	x %= y
	x &= y
	x |= y
	x ^= y
	x <<= y
	x >>= y


func literals():
	null # Null value
	false or true # Boolean values
	45 # Base 10 integer
	0x8f51 # Base 16 (hexadecimal) integer
	0b101010 # Base 2 (binary) integer
	3.14 or 58.1e-10 # Floating-point number (real)
	"Hello" + 'Hi' # Regular strings
	"""Hello""" + '''Hi''' # Triple-quoted regular strings
	r"Hello" + r'Hi' # Raw strings
	r"""Hello""" + r'''Hi''' # Triple-quoted raw strings
	&"name" # StringName
	^"Node/Label" # NodePath

	# There are also two constructs that look like literals, but actually are not:
	$NodePath # Shorthand for get_node("NodePath")
	%UniqueNode # Shorthand for get_node("%UniqueNode")

	12_345_678  # Equal to 12345678.
	3.141_592_7  # Equal to 3.1415927.
	0x8080_0000_ffff  # Equal to 0x80800000ffff.
	0b11_00_11_00  # Equal to 0b11001100.

	# Regular string literals can contain the following escape sequences:
	"\n \t \r \a \b \f \v \" \' \\ \u0000 \U000000"

# Annotations
@export_range(1, 100, 1, "or_greater")
var ranged_var: int = 50

const MAX_SPEED = 120.0
@export_range(0.0, 0.5 * MAX_SPEED)
var initial_speed: float = 0.25 * MAX_SPEED

@onready var my_label = get_node("MyLabel")


# In the Godot script editor, special keywords are highlighted within comments to bring the user's attention to specific comments:

# Critical (appears in red): ALERT, ATTENTION, CAUTION, CRITICAL, DANGER, SECURITY
# Warning (appears in yellow): BUG, DEPRECATED, FIXME, HACK, TASK, TBD, TODO, WARNING
# Notice (appears in green): INFO, NOTE, NOTICE, TEST, TESTING

## This comment will appear in the script documentation.
var value

## This comment will appear in the inspector tooltip, and in the documentation.
## They allow [b]bbcode[/b]
@export var exported_value: int


# Important: There must be *no* space between the `#` and `region` or `endregion`.

# This comment is outside the code region. It will be visible when collapsed.
#region Terrain generation
# This comment is inside the code region. It won't be visible when collapsed.
func generate_lakes():
	pass

func generate_hills():
	pass
#endregion

#region Terrain population
func place_vegetation():
	pass

func place_roads():
	pass
#endregion

func arrays():
	var arr2 = []
	arr2 = [1, 2, 3]
	var b = arr2[1] # This is 2.
	var c = arr2[arr2.size() - 1] # This is 3.
	var d = arr2[-1] # Same as the previous line, but shorter.
	arr2[0] = "Hi!" # Replacing value 1 with "Hi!".
	arr2.append(4) # Array is now ["Hi!", 2, 3, 4].

	var a: Array[int]
	var b2: Array[Node]
	var c2: Array[MyClass]
	var d2: Array[NamedEnum]
	var e: Array[Variant]

func dictionaries():
	var d = {4: 5, "A key": "A value", 28: [1, 2, 3]}
	d["Hi!"] = 0
	d = {
		22: "value",
		"some_key": 2,
		"other_key": [2, 3, 4],
		"more_key": "Hello"
	}

	# Lua-style table syntax is also supported.
	var d2 = {
		test22 = "value",
		some_key = 2,
		other_key = [2, 3, 4],
		more_key = "Hello"
	}

	var d3 = {} # Create an empty Dictionary.
	d.waiting = 14 # Add String "waiting" as a key and assign the value 14 to it.
	d[4] = "hello" # Add integer 4 as a key and assign the String "hello" as its value.
	d["Godot"] = 3.01 # Add String "Godot" as a key and assign the value 3.01 to it.


static var balance: int = 0

static var debt: int:
	get:
		return -balance
	set(value):
		balance = -value

class A:
	static var x = 1

class B extends A:
	pass

func _ready():
	prints(A.x, B.x) # 1 1
	A.x = 2
	prints(A.x, B.x) # 2 2
	B.x = 3
	prints(A.x, B.x) # 3 3


var lambda = func (x):
	print(x)

var lambda2 := func (x: int) -> void:
	print(x)


func my_func():
	pass

func self_references():
	print(self.my_var)

	my_func()
	self.my_func()


func control_flow():
	while (false):
		my_func()


	var thing
	match typeof(thing):
		TYPE_FLOAT:
			print("float")
		TYPE_STRING:
			print("text")
		TYPE_ARRAY:
			print("array")

	var point
	match point:
		[0, 0]:
			print("Origin")
		[_, 0]:
			print("Point on X-axis")
		[0, _]:
			print("Point on Y-axis")
		[var x, var y] when y == x:
			print("Point on line y = x")
		[var x, var y] when y == -x:
			print("Point on line y = -x")
		[var x, var y]:
			print("Point (%s, %s)" % [x, y])

var milliseconds: int = 0
var seconds: int:
	get:
		return milliseconds / 1000
	set(value):
		milliseconds = value * 1000


func get_my_prop():
	pass

func set_my_prop(val):
	pass

var my_prop:
	get = get_my_prop, set = set_my_prop

var my_prop2: get = get_my_prop, set = set_my_prop


func assertions():
	var enemy_power
	assert(enemy_power < 256, "Enemy is too powerful!")
