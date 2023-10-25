let btn = document.querySelector('.btn')
let content = document.querySelector('.content')
btn.addEventListener('click', () => {
    content.classList.add('active')
})

document.body.addEventListener('mouseover', () => {
    let del = setTimeout(() => {
        content.classList.remove('active')
    }, 2000);

    document.body.addEventListener('mouseout', () => {
        clearTimeout(del)
    })
})
