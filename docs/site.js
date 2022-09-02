(()=>{
  if (window.location.hash){
    const hash = window.location.hash.substring(1)

    displayTab(hash)
  }
  else {
    displayTab("about")
  }

  switchLang("cUrl")
})()

function displayTab(tab){
  if (tab === "about"){
    document.getElementById("aboutTab").hidden = false
    document.getElementById("docsTab").hidden = true
    document.getElementById("linkAboutTab").classList = "text-decoration-none"
    document.getElementById("linkDocsTab").classList = "text-decoration-none text-dark"
  }else if (tab === "docs"){
    document.getElementById("aboutTab").hidden = true
    document.getElementById("docsTab").hidden = false
    document.getElementById("linkAboutTab").classList = "text-decoration-none text-dark"
    document.getElementById("linkDocsTab").classList = "text-decoration-none"
  }
  location.hash = tab
}

function switchLang(lang){
  const codeList = document.querySelectorAll("[lang-tag]");

  for (let i of codeList) {
    if (i.attributes['lang-tag'].value === lang) {
      i.hidden = false

      continue
    }

    i.hidden = true
  }
}
