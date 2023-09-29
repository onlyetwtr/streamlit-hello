import streamlit as st
import matplotlib.pyplot as plt

def caffeine_calculator(caffeine_intake, half_life):
    total_hours = len(caffeine_intake)
    caffeine_in_body = [0] * total_hours

    # For each hour, calculate how the caffeine has decayed from previous hours
    for current_hour in range(total_hours):
        for intake_hour, intake in enumerate(caffeine_intake):
            time_since_intake = current_hour - intake_hour
            if time_since_intake >= 0:
                decayed_caffeine = intake * (0.5 ** (time_since_intake / half_life))
                caffeine_in_body[current_hour] += decayed_caffeine

    return caffeine_in_body

def main():
    st.title('Caffeine Calculator')

    caffeine_intake = []
    for i in range(24):  # Getting caffeine intake for the full 24-hour day
        hour_label = str(i) + ":00: "
        intake = st.number_input(hour_label, key=f'hour_{i}', value=0)
        caffeine_intake.append(intake)

    half_life = st.slider('Half-life of caffeine:', min_value=3, max_value=12, value=3)

    if st.button('Submit'):
        caffeine_over_time = caffeine_calculator(caffeine_intake, half_life)

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
