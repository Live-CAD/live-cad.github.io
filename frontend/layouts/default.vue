<template>
  <div>
    <header>
      <h1>My Nuxt 3 App</h1>
      <nav>
        <nuxt-link to="/">Home</nuxt-link>
        <nuxt-link to="/about">About</nuxt-link>
      </nav>
    </header>
    <main>
      <nuxt-page />
    </main>
    <footer>
      <p>&copy; 2025 My Nuxt 3 App</p>
    </footer>
  </div>
</template>

<style>
header {
  background-color: #333;
  color: white;
  padding: 1rem;
}
nav a {
  margin: 0 1rem;
  color: white;
  text-decoration: none;
}
footer {
  text-align: center;
  margin-top: 2rem;
  padding: 1rem 0;
  background-color: #f4f4f4;
}
</style>
