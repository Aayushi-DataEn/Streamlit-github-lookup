import os, requests, streamlit as st
st.image("github img.png")

# page_title = sets the browser tab title
st.set_page_config(page_title="GitHub Lookup")
st.title("🐙 GitHub User Lookup")

token = os.getenv("GITHUB_TOKEN")
headers = {"Accept": "application/vnd.github.v3+json"}
if token: headers["Authorization"] = f"token {token}"

user = st.text_input("GitHub username", "Aayushi-DataEn")

if st.button("Search"):
    try:
        response = requests.get(f"https://api.github.com/users/{user}", headers=headers, timeout=10)
        if response.status_code == 200:
            d = response.json()
            
            
            if d.get("avatar_url"): st.image(d["avatar_url"], width=160)
            st.write(f"*Name:* {d.get('name') or 'N/A'}")
            st.write(f"*Location:* {d.get('location') or 'N/A'}")
            st.write(f"*Company:* {d.get('company') or 'N/A'}")
            st.write(f"*Repos:* {d.get('public_repos',0)} | *Followers:* {d.get('followers',0)} | *Following:* {d.get('following',0)}")
            st.write(f"*Profile:* {d.get('html_url')}")
            
        elif response.status_code == 404:
            st.error(f"User '{user}' not found.")
            
        else:
            msg = (response.json().get("message") if response.headers.get("content-type","").startswith("application/json") else "Error")
            st.error(f"HTTP {response.status_code}: {msg}")
            
    except Exception as e:
        st.error(f"Error: {e}")
