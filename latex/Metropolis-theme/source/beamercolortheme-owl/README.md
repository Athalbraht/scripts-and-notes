# Beamer color theme `owl`

> The effectiveness of a colour scheme is heavily dependent on the conditions you present in. Colours that look nice on a computer screen may be invisible projected; colours that stand out in a lit room may strain the eyes in a dark room. If possible, you should carefully choose from Beamer's wide variety of colour themes to find one that fits your presentation's individual needs.


The above paragraph would be excellent advice, except for one thing --- only a handful of pre-selected colour themes are publicly available for Beamer. The vast majority of Beamer presentations use one of the [built-in colour themes](https://mpetroff.net/files/beamer-theme-matrix/), which are effective in some conditions but inadequate in others. The goal of this package is to reduce the number of situations you find yourself without any good colour options. `owl` is a flexible dark or light colour theme designed for maximum readability in environments where most themes fall flat.



## Examples

![The `owl` colour theme used with the Beamer themes `Hannover`, `Pittsburgh`, and `metropolis`](https://raw.githubusercontent.com/rchurchley/beamercolortheme-owl/master/ex/readme.jpg)



## Installation
Installing `owl`, as with any other LaTeX package, involves just three easy steps:

1. **Download the source** as a [zip archive](https://github.com/rchurchley/beamercolortheme-owl/archive/master.zip) or with a `git clone` of this Git repository.

2. **Compile** `beamercolorthemeowl.ins` with LaTeX to produce the package file `beamercolorthemeowl.sty`.

3. **Move the `.sty` file** to the folder containing your presentation or a directory in your TeX path.

That's it! We are working on a CTAN release which would make it even easier to
install through your LaTeX distribution's package manager.



## Usage

Once you have downloaded and installed the `beamercolorowl` package, using it is a piece of cake:

```latex
\usecolortheme{owl}
```

Unlike many Beamer themes, `owl` defaults to a dark theme with white text on a black background. This is particularly recommended for presentations with low ambient lighting, where it has the most advantages.

If you expect to present in a brightly-lit room or with a weak projector, you may wish to use to use the `snowy` option to use black text on a white background:

```latex
\usecolortheme[snowy]{owl}
```

In addition to setting the colour scheme of your slides, `owl` redefines the redefines the basic colour names `red`, `green`, `blue`, `yellow`, `violet`, `brown`, `orange`, and `cyan` to hues that are more visible when when displayed by some projectors. If you do not want these colour names to be redefined, use the `cautious` option when loading `owl`:

```latex
 \usecolortheme[cautious]{owl}
```

In either case, `owl`-defined colours will be available as `OwlRed`, `OwlGreen`, and so forth.

![`OwlRed`, `OwlGreen`, `OwlBlue`, and `OwlYellow`](https://raw.githubusercontent.com/rchurchley/beamercolortheme-owl/master/ex/colours.png)



## Contributions

The biggest way you can help `owl` is by sharing your experience using it. Our goal with `owl` is to provide colours that are as visible as possible, even in unfavourable presenting conditions, and that is very difficult to test with only one pair of eyes and a handful of projectors!

If you have used `owl` or seen it used, we would greatly appreciate your opinion on how it performed. Please open a GitHub Issue or privately email `ross@rosschurchley.com` with as much of the following information as you can:

- The version of `owl` used.
- The Beamer theme, if any, that was used together with `owl`.
- Whether `owl` was used as a dark or light theme.
- Details on the room (auditorium, large room, small room, ...)
- Details on the lighting conditions (brightly lit, dark, windows, ...)
- Details, if known, on the reporter's vision (glasses, colour deficiencies, ...)
- Your opinion on:
    + whether normal text was visible against the background.
    + whether the provided colours (`OwlRed`, `OwlBlue`, etc) were legible against the background.
    + whether the provided colours (`OwlRed`, `OwlBlue`, etc) were distinguishable from each other and from the normal text colour.

We also welcome technical feedback and bug reports in the form of GitHub Issues and pull requests. 
