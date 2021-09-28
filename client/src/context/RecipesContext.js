import React, { createContext, useContext, useMemo, useState } from "react";

const RecipesContext = createContext();

export const RecipesContextProvider = ({ children }) => {
  const [recipes, setRecipes] = useState([]);

  const routes = useMemo(() => {
    return { recipes, setRecipes };
  }, [recipes, setRecipes]);

  return (
    <RecipesContext.Provider value={routes}>{children}</RecipesContext.Provider>
  );
};

export const useRecipesContext = () => useContext(RecipesContext);
