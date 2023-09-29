import streamlit as st

def caffeine_calculator(caffeine_intake, bedtime, half_life):
    hours_to_bedtime = int(bedtime.split(':')[0])  # Now it starts from midnight

    caffeine_in_body = [0] * len(caffeine_intake)

    for i in range(len(caffeine_intake)):
        caffeine_in_body[i] += caffeine_intake[i]
        for j in range(i):
            caffeine_in_body[j] *= 0.5 ** (1 / half_life)

    caffeine_present = sum(caffeine_in_body[:hours_to_bedtime + 1])

    return f"The caffeine content in your body at bedtime is: {round(caffeine_present, 2)} mg"

def main():
    st.title('Caffeine Calculator')

    caffeine_intake = []
    for i in range(24):  # Getting caffeine intake for the full 24-hour day
        hour_label = str(i) + ":00: "
        intake = st.number_input(hour_label, key=f'hour_{i}', value=0)
        caffeine_intake.append(intake)

    bedtime = st.text_input('Bedtime (24h format):', value='22:00')
    half_life = st.number_input('Half-life of caffeine:', value=3)

    if st.button('Submit'):
        result = caffeine_calculator(caffeine_intake, bedtime, half_life)
        st.write(result)

if __name__ == '__main__':
    main()
