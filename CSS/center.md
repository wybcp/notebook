# [Centering in CSS](https://css-tricks.com/centering-css-complete-guide/)

## Horizontally

### inline or inline-\* elements

`text-align:center;`

This will work for inline, inline-block, inline-table, inline-flex, etc.

### a block element

it must has a `width` and set `margin` like `margin:0 auto;`.

### more block-level elements

make them a different `display` type.

#### horizontally in a row

##### inline-block example

```css
 {
  text-align: center;
} //parent container
 {
  display: inline-block;
} //element
```

##### flexbox example

```css
 {
  display: flex;
  justify-content: center;
} //parent container
```

#### multiple block level elements stacked on top of each other

the auto margin technique is fine like a block element.

## Vertically

### inline or inline-\* elements

- with a wrap: padding-top = padding-buttom

- no wrap: height = line-height

### multiple lines

#### vertical-align property

```html
<table>
  <tr>
    <td>
      verticle
    </td>
  </tr>
</table>

table td { /* default is vertical-align: middle; */ }
```

other way:

```html
<div class="center-table">
  <p>table</p>
</div>
.center-table { display: table; } .center-table p { display: table-cell;
vertical-align: middle; }
```

#### flexbox

A single flex-child can be made to center in a flex-parent.

```css
.flex-center-vertically {
  display: flex;
  justify-content: center;
  flex-direction: column;
  height: 400px;
}
```

#### the "ghost element" technique

```css
.ghost-center {
  position: relative;
}
.ghost-center::before {
  content: " ";
  display: inline-block;
  height: 100%;
  width: 1%;
  vertical-align: middle;
}
.ghost-center p {
  display: inline-block;
  vertical-align: middle;
}
```

### block-level element

#### know the height

```css
.parent {
  position: relative;
}
.child {
  position: absolute;
  top: 50%;
  height: 100px;
  margin-top: -50px; /* account for padding and border if not using box-sizing: border-box; */
}
```

#### unknown height

```css
.parent {
  position: relative;
}
.child {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
}
```

#### flexbox

```css
.parent {
  display: flex;
  flex-direction: column;
  justify-content: center;
}
```

## Both Horizontally and Vertically

You can combine the techniques above in any fashion to get perfectly centered elements. But I find this generally falls into three camps:

### fixed width and height

Using negative margins equal to half of that width and height, after you've absolutely positioned it at 50% / 50% will center it with great cross browser support:

```css
.parent {
  position: relative;
}

.child {
  width: 300px;
  height: 100px;
  padding: 20px;

  position: absolute;
  top: 50%;
  left: 50%;

  margin: -70px 0 0 -170px;
}
```

### unknown width and height If you don't know the width or height, you can use the transform property and a negative translate of 50% in both directions (it is based on the current width/height of the element) to center:

```css
.parent {
  position: relative;
}
.child {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}
```

### flexbox To center in both directions with flexbox, you need to use two centering properties:

```css
.parent {
  display: flex;
  justify-content: center;
  align-items: center;
}
```
