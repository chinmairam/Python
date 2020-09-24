## Import pathlib
@pytest.mark.test_site_path_import_module1

In this module we'll build up a `Site` Class that will set configuration values and create the root structure of our static site. 

We'll also create a command line tool using the `Typer` library. Since we are going to be working with paths, let's import `pathlib`, which is part of the standard library.

Open the `site.py` located in the `ssg` directory. At the top, import `Path` from `pathlib`.

## Create a class
@pytest.mark.test_site_class_module1
Below the import you just wrote, create a class called `Site`.
Next, create a `Site` class constructor that accepts three arguments `self`, `source`, and `dest`.
In the constructor, convert `source` to a `Path` object.
This can be done by passing it to a call to `Path()`.
Save the result to a class attribute with the same name. **Hint: class attributes are prefixed with `self`.**
Repeat these steps for `dest`.

## Find root directory
@pytest.mark.test_site_create_dir_function_module1
Still in the `Site` class, create a method called `create_dir()` that accepts two parameters, `self` and `path`.
In the body of the `create_dir` method, create a variable called `directory`. This variable will need to contain the full path to the destination folder.
The first part of the path is `self.dest`.
The second part of the path needs to be relative to `self.source`.
So after a `/` operator call `relative_to()` on `path` passing in `self.source`. **Hint: ` destination / relative_to()`.**

## Make a directory
@pytest.mark.test_site_create_dir_mkdir_module1
On a new line in the `create_dir()` method, call the `mkdir()` method on `directory`.
For our scenario we want `directory` to be replaced if it exists. Pass the following keyword arguments to `mkdir()`:

- `parents` set to `True`
- `exist_ok` set to `True`

## Make the destination directory
@pytest.mark.test_site_build_function_module1
Create a new method called `build()` in the `Site` class. Call the `mkdir()` method on `self.dest`.
As with the previous `mkdir()` call, pass the following keyword arguments to `mkdir()`:

- `parents` set to `True`
- `exist_ok` set to `True`

## Recreate all paths
@pytest.mark.test_site_path_rglob_module1
Still in the `build()` method, create a `for` loop that iterates through the paths of `self.source.rglob(*)`. Call the current iteration `path`. In the body of the `for` loop, test `if` the current `path` is a directory. If it is a directory, call the `create_dir()` method of the class, and pass in the current `path`.

## Import typer
@pytest.mark.test_ssg_imports_module1
Let's setup the command line interface (CLI). Open the `ssg.py` file in the root directory of the project. At the top, import `typer`. Also, import the `Site` class from `ssg.site`.

## Configuration options
@pytest.mark.test_ssg_main_command_module1
The Typer library requires a function that captures command line arguments. We'll call this function `main`. It should accept two keyword arguments: `source` with a default value of `"content"`, and `dest` with a default value of `"dist"`. In the body of the `main` function, create a dictionary called `config`. Add two key value pairs to `config`: `"source"` set to `source`, and `"dest"` set to `dest`.

## Build the site
@pytest.mark.test_ssg_build_call_module1
Still in the `main` function, create an instance of the `Site` class. The `Site` class requires that you provide two attributes `source` and `dest` when creating an instance. These are currently stored in the `config` dictionary as key value pairs. Unpack these dictionary values with `**` and pass it to the `Site` instance. Finally, chain a call to the `build()` method on this instance.

## Run typer
@pytest.mark.test_ssg_typer_run_module1
At the bottom of the file, call `typer.run()`, passing in the `main` function as its argument.


## Parser Class
@pytest.mark.test_parser_base_class_module2
In this module we will create a `Parser` base class that will have several functions that will help when converting Markdown and ReStructuredText to HTML.
To start, open the `ssg/parsers.py` file. We will add a few type annotations, one of which requires an import. Import `List` from `typing`. Also, import `Path` from `pathlib`.
 Next, create a class called `Parser`. Create a variable called `extensions` and assign it an empty list. Annotate `extensions` with the type `List[str]`.

## Validate Extensions
@pytest.mark.test_parser_valid_extension_function_module2
We will need to know whether certain files have a parser. This will be done by looking at the extension.
 Create a new method in the `Parser` class called `valid_extension()`. This method should accept an `extension`, and return whether or not that `extension` is `in` the class variable `self.extensions`. **Hint: This method is part of the `Parser` methods so it should accept `self` as an argument.**

## Base parse() method
@pytest.mark.test_parser_parse_function_module2
Since the `Parser` class is a base class, we will create a method that will need to be implemented in any subclass.
Call this method `parse()`, it should accept a `path`, `source`, and `dest`. Annotate each of these with the `Path` type.
In the body, `raise` the `NotImplementedError`.

## Parser read() method
@pytest.mark.test_parser_read_function_module2
The `Parser` class will need to be able to read the contents of a file.
  Create a method called `read()` that accepts a `path`. Use a `with` statement, and a call to `open()` to open `path` for reading `as` `file`.
In the body of the `with` statement, `return` what is `read()` from `file`.

## Parser write() method
@pytest.mark.test_parser_write_function_module2
Still in the `Parser` class, create a method called `write()` that accepts the following arguments: `path`, `dest`, and `content`. Also, add a parameter called `ext` with a default value of `".html"`.
In the body of the `write ` method, create a variable called `full_path`. This variable will need to contain the full path to the file being written to.
The first part of the path is `self.dest`.
 The second part names to be the name of the file with a new extension.
 So after a `/` operator, call `with_suffix()` on `path` passing in `ext`. Chain on the `name` property. **Hint: ` destination / with_suffix().name`.**

## Open file for writing
@pytest.mark.test_parser_write_function_open_module2
Still in the `write()` method, use `with` and `open()` to open `full_path` for writing `as` `file`.
In the body of the `with` statement, `write()` `content` to `file`.

## Parser copy() method
@pytest.mark.test_parser_copy_function_module2
Move back to the top of the page and import `shutil`. We'll this use this library to copy resources to the correct location.
Below the exiting methods in the `Parser` class, create a new method called `copy()`.
This method should accept the following arguments `path`, `source`, and `dest`.
In the body use the `copy2` method (from the `shutil` module) to copy the file at `path` to the correct location in the destination folder structure.
 This can be done by passing `path` as the first argument to `copy2` and the second argument is made up of  the `dest` `/` and the `path` relative to the `source`.

## ResourceParser subclass
@pytest.mark.test_parser_resource_class_module2
Create a class called `ResourceParser` that is a sub-class of `Parser`.
Create a class attribute called `extensions` and assign it a list with five extensions, `".jpg"`, `".png"`, `".gif"`, `".css"`, and `".html"`.
Implement the `parse()` method in the `ResourceParser` class. It should have the same signature as in the base class `Parser`.
In the body, call the inherited `copy()` method. Which is  inherited from `Parser`. Pass in `path`, `source`, and `dest` to `copy()`.

## Available parsers
@pytest.mark.test_site_parsers_module2
Open `ssg/site.py`, and add a parameter to the constructor parameter list called `parsers`. Set the default value to of `parsers` to `None`.
In the body of the constructor, set a new instance variable called `parsers` to the expression `parsers or []`.

## Parser configuration
@pytest.mark.test_ssg_config_parser_module2
Open `ssg.py`, and at the top import `ssg.parsers`.
Find the `config` dictionary in the `main` function and add a new key value pair as follows:  - Key - `parsers` - Value - `ssg.parsers.ResourceParser()`.

## Site class load_parser() method
@pytest.mark.test_site_load_parser_module2
Back in `ssg/site.py`, add a new method to the `Site` class called `load_parser()` below the existing methods. This method should accept a single parameter called `extension`.
The first statement in the method should be a `for` loop that cycles through `self.parsers`. Call the loop-value `parser`.
The body of the `for` loop should have an `if` statement that tests if `extension` is a `valid_extension()`. **Hint: `parser` is an instance of the `Parser` class, so it will have a `valid_extension()` method.**   Return `parser` in the `if` statement.

## Site class run_parser() method
@pytest.mark.test_site_run_parser_module2
Still in the `Site` class, add a new method called `run_parser()`. This method should accept a parameter called `path`.
In this method, call `load_parser()`, passing in `path.suffix`, and save the result to a variable called `parser`.

## Call the parse() method
@pytest.mark.test_site_run_parser_if_module2
Still in the `run_parser()` method, test if `parser` is not `None`. If parser is not `None`, then call the `parse()` method of `parser`.
Pass `path` as the first argument to the `parse()` method. Then, pass `source` and `dest`, both of which are instance variables to the `parse()` method.
  Add an `else` to the `if` that prints the message `Not Implemented`.

## Run the parser
@pytest.mark.test_site_build_elif_module2
To connect everything together, find the `if` statement in the `build()` method. Add an `elif` that tests whether `path` is a file.
If `path` is a file, then call `run_parser()`, passing in `path`. **Hint: `run_parser()` is part of the `Site` class.**


## Imports
@pytest.mark.test_content_imports_module3
When creating content we can add metadata to our files using YAML. YAML is a human friendly data format https://yaml.org/. To see an example open the `index.md` file in the `content` directory. The section at the top delimited by `---` is called YAML frontmatter. We'll extract this data from each file in our site. This will be done by splitting the contents of a file on two possible delimiters `---` and `+++`.
 This will require the use of regular expressions and the `pyyaml` library. Import `re` from the standard library and import `load` and `FullLoader` from `yaml`.
We will also need the `Mapping` collection class, import it from `collections.abc`.

## Content class
@pytest.mark.test_content_class_module3
Below the imports, create a class called `Content`, and make sure that it inherits from `Mapping`.
  In the new class, create a class variable called `__delimeter`, and assign it the raw string `"^(?:-|+){3}\s*$"`.
 Create another class variable called `__regex`, assign it the result of a call to `re.compile()`, and pass it `__delimiter` and the constant `re.MULTILINE`.

## Load class method
@pytest.mark.test_content_classmethod_load_module3
Create a new method called `load()` in the `Content` class, and make it a class method with the appropriate decorator. This method should accept two parameters, `cls` and `string`.
 In the body of the `load()` method, call `split()` on the `__regex` class variable, passing in `string` and a depth of `2`. Assign the result of this to three variables `_, fm, content`.
Next, on a new line, call `load()` and pass in `fm` and a keyword argument of `Loader` set to `FullLoader`. Finally, return a call to `cls()`, and pass in `metadata` and `content`.

## Content constructor
@pytest.mark.test_content_init_module3
Create a `Content` class constructor below the `load()` method. The constructor should accept two parameters, `metadata` and `content`. Create a class attribute named `data`, and assign it `metadata`.
On a new line, add a key value pair to `self.data` of `"content"` set to `content`.

## Body property
@pytest.mark.test_content_body_property_module3
Still in the `Content` class, add a class `@property` of `body()` that returns `self.data["content"]`.

## Type property
@pytest.mark.test_content_type_property_module3
Also in the `Content` class, add a class `@property` of `type()` that returns `self.data["type"]` if `self.data` has a key of `type`. If that key doesn't exist, then return `None`. This needs to be done with a ternary `if`.

## Type setter
@pytest.mark.test_content_type_setter_module3
Create a `setter` for the `type()` `@property` that assigns to `self.data["type"]`.

## Custom getitem method
@pytest.mark.test_content_getitem_module3
Let's implement a custom `__getitem__()` method so that it returns the value from `self.data[]` for the `key` that is provided.

## Custom iterator method
@pytest.mark.test_content_getitem_module3
The `Content` class will also have a custom `__iter__()` method that calls `self.data`s iterator method.

## Custom length method
@pytest.mark.test_content_len_module3
We'll also need a custom `__len__()` method that returns the length of `self.data`.

## Content representation
@pytest.mark.test_content_repr_module3
The final custom method that we will implement is the `__repr__()` method. It will create a custom representation of `self.data`. Create a `__repr__()` method, and on the first line create an empty dictionary called `data`. Return a call to `str()`, passing in `data`.

## Removing content from the representation
@pytest.mark.test_content_repr_for_loop_module3
We would like the custom representation to include only certain values. Loop through `self.data.items()` with a `for` loop. The current key should be called `key`, and the value should be `value`. In the `for` loop, test if `key` is not equal to `"content"`. In the `if`, assign the `value` to `data[key]`.


## Markdown and ReStructuredText imports
@pytest.mark.test_parser_imports_module4
In this module we will convert Markdown and ReStructuredText to HTML. Open the `ssg/parsers.py` file and at the top around the existing imports,  import the following:  - `sys` - `publish_parts` from `docutils.core` - `markdown` from `markdown` - `Content` from `ssg.content`

## Markdown Parser
@pytest.mark.test_parser_markdown_class_module4
We have already created a `Parser` sub-class. Let's create another subclass called `MarkdownParser`. With in the new `MarkdownParser` class, create a variable called `extensions`. This should be assigned a list with the extensions `".md"` and `".markdown"`.

## Markdown parse() method
@pytest.mark.test_parser_markdown_parse_module4
Implement the `parse()` method in the `MarkdownParser` class. It should have the same signature as in the base class. In the body, call the `Content.load()` class method, pass in a call to `self.read()`, and to that pass `path`. Assign the result to a variable called `content`.

## Converting markdown to html
@pytest.mark.test_parser_markdown_parse_write_html_module4
In the body of the `parse()` method, call the `markdown()` method and pass in `content.body`. Assign the results to a variable called `html`. Use `self.write()` to write `html` to `path` at `dest`.
As the last call in the `parse()` method, call `sys.stdout.write()`. Pass it the string `"\x1b[1;32m{} converted to HTML. Metadata: {}\n"`, append a call to `format()`, and pass in `path.name` and `content`. _Note: The string `\x1b[1;32m` changing the color of the printed string in the terminal to green._

## ReStructuredText parser
@pytest.mark.test_parser_restructuredtext_class_module4
Create another subclass called `ReStructuredTextParser`. Within the new `ReStructuredTextParser` class, create a variable called `extensions`. This should be assigned a list with the extension `".rst"`.

## ReStructuredText parse() method
@pytest.mark.test_parser_restructuredtext_parse_module4
Implement the `parse()` method in the `ReStructuredTextParser` class. It should have the same signature as in the base class.
In the body, call the `Content.load()` class method and pass in a call to `self.read()`, and to that pass `path`. Assign the result to a variable called `content`.

## Converting ReStructuredText to html
@pytest.mark.test_parser_restructuredtext_parse_write_html_module4
In the body of the `parse()` method, call the `publish_parts()` method and pass in `content.body`. Also add a keyword argument of `writer_name` set to `"html5"`.
 Assign the results to a variable called `html`. Use `self.write()` to write `html["html_body"]` to `path` at `dest`.
 As the last call in the `parse()` method, call `sys.stdout.write()`. Pass it the string `"\x1b[1;32m{} converted to HTML. Metadata: {}\n"`, append a call to `format()`, and pass in `path.name` and `content`.

## Add available parsers
@pytest.mark.test_ssg_parsers_array_module4
Open the `ssg.py` file at the root of the project, and find the `parsers` list in the `config` dictionary. Add both `ssg.parsers.MarkdownParser()` and `ssg.parsers.ReStructuredTextParser()` to the list.

## Error reporting @staticmethod
@pytest.mark.test_site_staticmethod_module4
Switch over to `ssg/site.py`, and at the top import `sys`.
 Then, below all other methods in the `Site` class, create a static method called `error()`, and give it a `@staticmethod` decorator.
Since this is a static method, it does not need to accept `self`, but it does need to accept a parameter of `message`.
 In the body of the `error()` method, call the `sys.stderr.write()` method. Pass in the string `"\x1b[1;31m{}\n"`, append a call to `format()` and pass in `message`.

## Calling error @staticmethod
@pytest.mark.test_site_error_call_module4
Find the `run_parser()` method in the `Site` class, and replace the `print()` call with a call to `self.error()`.
Then, pass in the message `"No parser for the {} extension, file skipped!"`. Append to this string a call to `format()`, passing in `path.suffix`.

