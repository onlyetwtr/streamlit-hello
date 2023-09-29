import streamlit as st
import matplotlib.pyplot as plt

def caffeine_calculator(caffeine_intake, bedtime, half_life):
    hours_to_bedtime = int(bedtime.split(':')[0])

    caffeine_in_body = [0] * len(caffeine_intake)

    for i in range(len(caffeine_intake)):
        caffeine_in_body[i] += caffeine_intake[i]
        for j in range(i):
            caffeine_in_body[j] *= 0.5 ** (1 / half_life)

    caffeine_present = sum(caffeine_in_body[:hours_to_bedtime + 1])

    return caffeine_in_body, f"The caffeine content in your body at bedtime is: {round(caffeine_present, 2)} mg"

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
        caffeine_over_time, result = caffeine_calculator(caffeine_intake, bedtime, half_life)
        st.write(result)

        # Plotting the caffeine content and raw intake over time
        hours = [str(i) + ":00" for i in range(24)]
        fig, ax = plt.subplots()
        ax.plot(hours, caffeine_over_time, label='Caffeine Content in Body', color='blue')
        ax.plot(hours, caffeine_intake, label='Raw Caffeine Intake', linestyle='dotted', color='red')
        ax.set_xlabel('Hour')
        ax.set_ylabel('Caffeine Content (mg)')
        ax.set_title('Caffeine Content and Intake Over Time')
        ax.grid(True)
        ax.legend()
        ax.set_xticks([str(i) + ":00" for i in range(0, 24, 2)])  # Displaying every 2nd hour for clarity
        ax.set_xticklabels([str(i) + ":00" for i in range(0, 24, 2)], rotation=45)  # Rotating labels for clarity
        st.pyplot(fig)

if __name__ == '__main__':
    main()
