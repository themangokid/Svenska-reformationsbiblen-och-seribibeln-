# Swedish Bible LaTeX Project 📖

A comprehensive LaTeX document for generating beautifully formatted Swedish Bible texts with professional typography and mobile-responsive layouts.

### Mobile Layout

To enable mobile-optimized formatting, change this line in the document:

```latex
% Change from:
\mobilelayoutfalse

% To:
\mobilelayouttrue
```

### Including All Books

To include all New Testament books, modify:

```latex
% Change from:
\allbooksfalse

% To:
\allbookstrue
```

## 📁 Project Structure

```
swedish-bible-latex/
├── main.tex                    # Main document file
├── front-page/
│   ├── title_text_gamla_testamentet.tex
│   ├── title_text_nya_testamentet.tex
│   └── icons_low_quality.tex
├── render/
│   ├── GT/                     # Gamla Testamentet (Old Testament)
│   │   ├── Forsta_Moseboken.tex
│   │   └── Andra_Moseboken.tex
│   └── NT/                     # Nya Testamentet (New Testament)
│       ├── matteus.tex
│       ├── markus.tex
│       ├── lukas.tex
│       └── ...
└── README.md
```

## 🎨 Customization

### Colors

The document uses three main colors defined in the preamble:

```latex
\definecolor{oldpaper}{RGB}{250, 240, 210}    % Background
\definecolor{textcolor}{RGB}{0, 0, 0}         % Text
\definecolor{titlecolor}{RGB}{90, 50, 30}     % Titles/Links
```

### Page Dimensions

#### Desktop Layout:
```latex
paperwidth=6.5in
paperheight=9.5in
```

#### Mobile Layout:
```latex
paperwidth=4in
paperheight=7in
```

### Font Settings

```latex
\setmainfont[UprightFeatures={FakeBold=1.12}]{EB Garamond}
\renewcommand{\normalsize}{\fontsize{16pt}{20pt}\selectfont}
```

## ✨ Features Detail

### 🔤 Drop Caps (Lettrine)

Special formatting for chapter beginnings with custom settings for the letter "J":

```latex
\IfStrEq{\firstletter}{J}{%
    \lettrine[loversize=0.21, lines=3, lraise=0.22]{\firstletter}{\textsc{\firstword}}
}{%
    \lettrine[loversize=0.3, lines=3, lraise=0.01]{\firstletter}{\textsc{\firstword}}
}
```

### 🔗 Interactive Links

All external links open in new tabs/windows:

```latex
\href[pdfnewwindow=true]{URL}{Link Text}
```

### 📱 Responsive Design

Automatic layout switching between desktop and mobile formats based on the `\ifmobilelayout` conditional.

### 🎯 Navigation

- Clickable table of contents
- "Back to TOC" links throughout the document
- Hyperlinked cross-references

## 🌐 External Resources

The document includes quick links to:

- **[Bibel.se](https://bibel.se/)** - Main Swedish Bible website
- **[Bibelonline](https://bibelonline.se/biblereader.php)** - Online Bible reader
- **[SRB Bibelböcker](https://bibel.se/wordpress/index.php/2022/01/18/oversatta-bibelbocker/)** - Translated Bible books
- **[Google Drive](https://drive.google.com/drive/folders/1N-suLiCB4gOavhUg04P0xGzSDlCSntgo)** - Collected materials
- **[Seriebibeln](https://seriebibeln.com/kristna-serier)** - Christian comics
- **[Audio Bible](https://www.youtube.com/@reformationsbibeln9676/videos)** - YouTube audio Bible
