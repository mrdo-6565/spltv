import streamlit as st

import numpy as np

st.write("Kalkulator PLTV created by Mr Do")

def solve_linear_system(coeff_matrix, const_matrix):
    try:
        solution = np.linalg.solve(coeff_matrix, const_matrix)
        return solution
    except np.linalg.LinAlgError:
        return None

def main():
    st.title("Kalkulator Persamaan Linier Tiga Variabel")
    st.write("Masukkan koefisien dan konstanta untuk tiga persamaan:")
    st.write("a1x + b1y + c1z = d1")
    st.write("a2x + b2y + c2z = d2")
    st.write("a3x + b3y + c3z = d3")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.write("Koefisien x")
        a1 = st.number_input("a1", value=1.0)
        a2 = st.number_input("a2", value=1.0)
        a3 = st.number_input("a3", value=1.0)
    
    with col2:
        st.write("Koefisien y")
        b1 = st.number_input("b1", value=1.0)
        b2 = st.number_input("b2", value=1.0)
        b3 = st.number_input("b3", value=1.0)
    
    with col3:
        st.write("Koefisien z")
        c1 = st.number_input("c1", value=1.0)
        c2 = st.number_input("c2", value=1.0)
        c3 = st.number_input("c3", value=1.0)
    
    with col4:
        st.write("Konstanta")
        d1 = st.number_input("d1", value=1.0)
        d2 = st.number_input("d2", value=1.0)
        d3 = st.number_input("d3", value=1.0)
    
    if st.button("Hitung Solusi"):
        coeff_matrix = np.array([[a1, b1, c1], [a2, b2, c2], [a3, b3, c3]])
        const_matrix = np.array([d1, d2, d3])
        
        solution = solve_linear_system(coeff_matrix, const_matrix)
        
        if solution is not None:
            st.success(f"Solusi: x = {solution[0]}, y = {solution[1]}, z = {solution[2]}")
        else:
            st.error("Sistem tidak memiliki solusi unik atau tidak dapat diselesaikan.")

if __name__ == "__main__":
    main()
