def solution(s):
    st = s

    st = st.replace('zero', '0')
    st = st.replace('one', '1')
    st = st.replace('two', '2')
    st = st.replace('three', '3')
    st = st.replace('four', '4')
    st = st.replace('five', '5')
    st = st.replace('six', '6')
    st = st.replace('seven', '7')
    st = st.replace('eight', '8')
    st = st.replace('nine', '9')

    answer = int(st)

    return answer
