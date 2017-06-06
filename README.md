# Django Component Library

*A framework for creating a living component library with Django.*

This repository is a demonstration of how to set up a component library using Django.

Building a frontend using components allows code reuse throughout a project.

Django can construct an application from these components.

This example scans the `/frontend/components` directory and builds demo pages automatically.


## Requirements

- `python 3`
- `node 7+`

## Install

- `pip install -r requirements.txt`

## Running

During development, run the following two commands in two terminal windows simultaneously:

1. from the root `/` directory:
  ```
  npm start
  ```

2. from the `/dcl` directory:
  ```
  ./manage.py runserver
  ```

Once running, you can browse the demo site at [http://localhost:8000/](http://localhost:8000/) and see the component library at [http://localhost:8000/components/](http://localhost:8000/components/)


## Components

A component-based architecture means any part of the website can be worked on in isolation, safe in the knowledge that it can be developed, tested and used without impacting on any other part of the website.


### Directory structure

Each component should follow a similar directory structure for its frontend files:

```
/frontend/components
  |-- /[group]
  |    |-- /ComponentName
  |    |    |-- ComponentName.js  
  |    |    |-- ComponentName.css
  |    |    |-- ComponentName.html
  |    |    |-- demo/
  |    |    |    |-- demo.json
  |    |    |    |-- demo.html
  |    |    |-- tests/
  |    |    |    |-- ...

```


### Naming conventions

[SuitCSS](https://github.com/suitcss/suit/blob/master/doc/naming-conventions.md) naming conventions should be followed for all components.


### Templates

Each template should start and end with a single wrapping HTML element, that should contain the class name of the component.

```
<div class="ComponentName">
    ...
</div>
```


### CSS

Every component CSS file should contain styles targeting only the component itself.  


#### Style isolation

Other than a CSS reset, there are no global styles that are inherited by all components.

This allows components to be developed in isolation, safe in the knowledge that they won't inherit styles when incorporated into the site.


#### Linting

All component CSS is linted to ensure conformance with SuitCSS naming conventions.

The top of every component CSS file should contain the following comment to enable linting:

```
/**
 * @define ComponentName
 */
```

If a file contains styles that _need_ to break the SuitCSS rules, there are two options.

SuitCSS conformance checking can be relaxed for the file, by adding `weak` to the initial component declaration:

```
/**
 * @define ComponentName; weak
 */
```

For further information on this, see the [postcss-bem-linter](https://github.com/postcss/postcss-bem-linter#defining-a-component) documentation.

Alternatively, linting can be disabled within a file (altogether, or just for specific rules)

```
/* stylelint-disable */
.ComponentName {}
/* stylelint-enable */
```

For further information on this, see the [stylelint](http://stylelint.io/user-guide/configuration/#turning-rules-off-from-within-your-css) documentation.


### JS

No JavaScript conventions are dictated. However, a component-based approach is recommended.

All JavaScript added is linted using [ESLint](http://eslint.org/), using [standard](https://standardjs.com/) conventions.


### Demo

A `/demo` directory within each component provides a standalone implementation of the component, providing an HTML page and JSON data used to render the component.

It should demonstrate how to use the component. Every possible modifier should be demonstrated to showcase all available states.

### Mapping Django models to components

Components may only need some of a model's fields or may need some dynamic fields generated from the model's data (e.g. a URL to a resized thumbnail for an image).

Using [Django Rest Framework](http://django-rest-framework.org) serializers data can be prepared for components. An example can be seen in the `articles` app within this project. The `ArticleDemoThumbSerializer` takes the `Article` model and serializes it for the `DemoThumb` component.

Using serializers means this serialization is moved out of the individual views and can be shared between other views which also use this component.

Serializers should be named with the model name and then the component name in the following format `<model name><component name>Serializer`


### Further reading

- [http://webdesign.tutsplus.com/tutorials/using-postcss-with-bem-and-suit-methodologies--cms-24592](http://webdesign.tutsplus.com/tutorials/using-postcss-with-bem-and-suit-methodologies--cms-24592)
- [http://csswizardry.com/2015/06/contextual-styling-ui-components-nesting-and-implementation-detail/](http://csswizardry.com/2015/06/contextual-styling-ui-components-nesting-and-implementation-detail/)
- [https://benfrain.com/enduring-css-writing-style-sheets-rapidly-changing-long-lived-projects/](https://benfrain.com/enduring-css-writing-style-sheets-rapidly-changing-long-lived-projects/)
- [http://philipwalton.com/articles/side-effects-in-css/](http://philipwalton.com/articles/side-effects-in-css/)


#### Selected quotes

> BEM was the forerunner of this type of class naming methodology, created by Yandex. The SUIT methodology is an approach based on BEM, but with some adjustments and additions made by Nicholas Gallagher. SUIT does everything BEM does, but to many users it is considered an enhancement.
>
> ```
> /* BEM */
> .search-form__text-field {}
>
> /* SUIT */
> .SearchForm-textField {}

[http://webdesign.tutsplus.com/tutorials/using-postcss-with-bem-and-suit-methodologies--cms-24592](http://webdesign.tutsplus.com/tutorials/using-postcss-with-bem-and-suit-methodologies--cms-24592 )

> The notion that all UI components are born equal—and should be able to exist anywhere, at any time, and independently—is a huge move forward for UI developers in terms of the consistency and quality of the products we work with.

[http://csswizardry.com/2015/06/contextual-styling-ui-components-nesting-and-implementation-detail/](http://csswizardry.com/2015/06/contextual-styling-ui-components-nesting-and-implementation-detail/)

> Two years ago I wrote a book where I was preaching DRY code, but after working on enduring projects, it's "decoupling" that became more important to me.

[http://ecss.io/chapter3.html](http://ecss.io/chapter3.html )

> I wasn't convinced that the goal of DRY code that other CSSers were pursuing and extolling the virtues of, was the same kind of DRY code I wanted. To explain that a little more - I didn't care much about repeated values and pairs across my rules, which is what most people were concentrating on DRYing out. What I cared about was key selectors not being repeated in the codebase. Key selectors were my 'single source of truth' and that was the area I wanted to DRY out.

>if a component needs to be made that is similar, yet subtly different to an existing component, we would not abstract or extend from this existing component. Instead, a new one would be written. Yes, I'm serious. Even if 95% of it is the same.

>The benefit of this is that each component is then independent and isolated. One can exist without the other. One can change however it needs to, independently from the other. Despite their apparent aesthetic similarity at the outset, they can mutate as needed with no fear of infecting or tainting any other similar looking component. To extend the biological metaphor, we have gained components that are 'self-quarantining' by virtue of their unique namespace.

[http://ecss.io/chapter4.html](http://ecss.io/chapter4.html)

> With the exception of intentionally 'global' CSS, all code that relates to the presentation of a component or module should be included in the partials that sit alongside the HTML/JS of that component.

> The code for each component becomes physically self-enclosed. Then, on our enduring project, when features need changing or are deprecated, all associated code for that module (styles, view logic (HTML) and JS) can be easily updated/removed.

[http://ecss.io/chapter5.html](http://ecss.io/chapter5.html)

> Typically, my foremost goal when writing CSS for enduring and rapidly changing web application is long-term maintainability. As a concrete example; being able to delete an entire Sass partial (say 9KB) in six months time with impunity (in that I know what will and won’t be affected by the removal) is far more valuable to me than a 1KB saving enjoyed because I re-used or extended some vague abstracted styles.
>
> For me, a larger total CSS codebase, made up of components that are in many respects insulated from one another, is preferential to a smaller CSS codebase made up of inter-dependent and intrinsically related styles. Hopefully I can justify and legitimise this stance further shortly.

[https://benfrain.com/enduring-css-writing-style-sheets-rapidly-changing-long-lived-projects/](https://benfrain.com/enduring-css-writing-style-sheets-rapidly-changing-long-lived-projects/)

> Because all CSS rules live in the global scope, side effects are extremely common. And since your average stylesheet usually consist of an extremely fragile collection of highly-coupled rules, all intimately dependent on the presence, order, and specificity of other rules, even the most unassuming changes can have unforeseen consequences.

> I said above that all CSS rules are global and every rule has the potential to conflict with every other rule on the page. This means side effects cannot be prevented by the language; however, they can be prevented via a disciplined and enforceable naming convention. And that’s exactly what BEM provides.

[http://philipwalton.com/articles/side-effects-in-css/](http://philipwalton.com/articles/side-effects-in-css/)

> A few bullet points of things we've learned to be important when building component libs:
>
> - Co-locating everything to do with a single component is really nice. Put the template, CSS, logic, functional tests, unit tests and any other assets related to the component (SVGs, images etc.) in the same folder. Put any files needed to demo the component in the same folder too, possibly in a subfolder called "demo" or similar
>
> - When you're working on a component and you only need to look inside its folder to understand it, literally nowhere else in the project, it's a huge win. Global CSS files, shared CSS variables, shared assets and any other project-wide abstractions can all make things much more complicated than they need to be. Copy and pasting some CSS, or updating a SVG in a component folder is cheap, but trying to understand the library-wide ramifications of a CSS tweak that affects many components is a nightmare.
>
> - Try and encapsulate your components as much as possible at all times, and think about what API it exposes to the outside world. Components that just let themselves be customised via props and limited API surface are easier to document, think about and test that components that let the outside world affect them via externally applied CSS classes etc
>
> - Use flexbox liberally inside components for internal layout. Don't worry too much about large-scale layout abstraction CSS in the component library, this sort of CSS should be in the domain of the client apps ... and you can use flexbox for this too!
>
> - Webpack and CSS Modules are great for this sort of thing, but probably only apply if you're making JS components for use in frameworks like React or Angular
>
> - Webpack is neat because it can output the entire component library (JS, CSS, assets, logic) in a single UMD JS bundle which makes consuming the components as easy as adding a single `<script>` tag to your client app
Publishing a component lib as a private npm module using semver is a neat way of getting control and understanding of the release process and the various versions you're maintaining in client apps

> - Don't spend any time making the demo site look pretty, rather it should be a functional developer tool that documents the various ways components can be used. If you need to make a "pretty styleguide" site in future, say for marketing purposes, then if your components are properly re-usable then this should be a doddle and can be created as a standalone thing
