import plotly.express as px

gapminder = px.data.gapminder().query("country=='Canada'")
fig = px.line(gapminder, x="year", y="lifeExp", title="Life")
fig.show()