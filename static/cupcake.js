mybtn = document.querySelector(".buttons");

mybtn.addEventListener("click", removeCupcake);

async function removeCupcake(e) {
  childElement = e.target;
  childId = childElement.parentElement.id;
  await axios.delete(`/api/cupcakes/${childId}`);
  childElement.parentElement.remove();
}
