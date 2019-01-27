### How to install npm?
install node.js. it will automatically install npm
### How to update npm?
```
  npm install -g npm
```
### How to install react?
```
npm install -g create-react-app@1.5.2
```
where g means global, @1.5.2 means to install version 1.5.2

###  How to create react app
```
create-react-app react-app
```
where react-app is the name of the application. If create-react-app is not found. set up path.

This will install react and other third party libraries including
1. Development Server
2. Webpack
3. Babel

### How to run react app?
```
npm start
```

by default it will run on port 3000

### How to install bootstrap uisng npm
```
npm i bootstrap@4.1.1
```

### How to import bootstrap in react application
add in index.js
```
import "bootstrap/dist/css/bootstrap.css";
```

### shortcut for reacts
```
imrc
cc
```

### What is export default Counter?
it is useful when importing. we dont have to put curl braces around counter if we use export default counter

### what if i dont want to have extra wrapper.
well you can use React.Fragment

### when extending a class we have to call super to call the constrcutor of the parent class
