import webbrowser
import requests

def verificar_perfil(url):
    try:
        response = requests.get(url, timeout=5)
        return response.status_code == 200
    except requests.RequestException:
        return False

def buscar_redes_sociales(nombre_usuario):
    plataformas = {
        "Gmail": f"mailto:{nombre_usuario}@gmail.com",
        "Instagram": f"https://www.instagram.com/{nombre_usuario}/",
        "Facebook": f"https://www.facebook.com/{nombre_usuario}",
        "X (Twitter)": f"https://twitter.com/{nombre_usuario}"
    }
    
    perfiles_encontrados = {}
    
    for plataforma, url in plataformas.items():
        if "mailto" in url or verificar_perfil(url):
            perfiles_encontrados[plataforma] = url
    
    return perfiles_encontrados

if __name__ == "__main__":
    nombre_usuario = input("Introduce tu nombre de usuario: ")
    perfiles = buscar_redes_sociales(nombre_usuario)
    
    if perfiles:
        print("Perfiles encontrados:")
        for plataforma, url in perfiles.items():
            print(f"{plataforma}: {url}")
            #webbrowser.open(url)
    else:
        print("No se encontraron perfiles.")
