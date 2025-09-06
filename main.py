import asyncio, logging, pyautogui, pynput, sys
from data import GamePositions, SettingsPositions, GeneralScreenPositions, AppPositions
logging.basicConfig(format='[%(asctime)s] %(message)s', datefmt='%H.%M.%S', level=logging.INFO)
gamePositions, settingsPositions, generalPositions, appPositions, shutdownFlag = GamePositions(), SettingsPositions(), GeneralScreenPositions(), AppPositions(), False



async def executionDelay(delayInSeconds: int) -> None:
    await asyncio.sleep(delayInSeconds)

async def clickScreenPositionWithDelay(positionToClick: tuple, loggingMessage: str = None, delayInSeconds: float = 1.5) -> None:
    await executionDelay(delayInSeconds)
    pyautogui.moveTo(positionToClick, duration=1)
    pyautogui.click()
    if loggingMessage:
        logging.info(loggingMessage)

async def clickThenTypeTextWithDelay(textToWrite: str, loggingMessage: str = None, delayInSeconds: float = 1.5) -> None:
    await executionDelay(delayInSeconds)
    await executionDelay(4)
    pyautogui.typewrite(textToWrite)
    if loggingMessage:
        logging.info(loggingMessage)

def on_press(key):
    global shutdownFlag
    try:
        if key.char and key.char.lower() == 'c':
            logging.info("Shutdown key 'C' pressed. Shutting down program...")
            print("Shutdown key 'C' pressed. Shutting down program...")
            shutdownFlag = True
    except AttributeError:
        # Special keys (ctrl, alt, etc.) don't have char attribute
        pass

async def startKeyboardListener():
    """Start the keyboard listener in a separate thread"""
    listener = pynput.keyboard.Listener(on_press=on_press)
    listener.start()
    return listener

async def main():

    listener = await startKeyboardListener()
    logging.info("Keyboard listener started. Press 'C' to shutdown the program.")
    print("Keyboard listener started. Press 'C' to shutdown the program.")
    
    async def automateIdleMinerTycoon():
        # Check shutdown flag before each major operation
        if shutdownFlag: return

        # Collect 2x Rewards Button
        await clickScreenPositionWithDelay(gamePositions.collect_2x_rewards, "Collect 2x Rewards Button Clicked")

        if shutdownFlag: return

        # Confirm Collect 2x Rewards Button
        await clickScreenPositionWithDelay(gamePositions.collect_2x_rewards_confirm, "Collect 2x Rewards Confirmed")

        if shutdownFlag: return
            
        # Go to Home Menu
        await clickScreenPositionWithDelay(generalPositions.exit_bar_bottom, "Home Menu Button Clicked")

        if shutdownFlag: return
            
        #Open Settings Application
        await clickScreenPositionWithDelay(appPositions.settings, "Settings Application Button Clicked")

        if shutdownFlag: return
            
        # Go to Settings Application Search Bar
        await clickScreenPositionWithDelay(settingsPositions.search_bar, "Settings Application Search Bar Clicked")

        if shutdownFlag: return

        # Type "Date" in Search Bar to find Date & Time Settings
        await clickThenTypeTextWithDelay("Date", "Searched for Date in Settings")

        if shutdownFlag: return
            
        # Open Date & Time Settings
        await clickScreenPositionWithDelay(settingsPositions.date_time, "Opened Date & Time Settings")

        if shutdownFlag: return

        # Toggle Automatic Date & Time Off
        await clickScreenPositionWithDelay(settingsPositions.auto_toggle, "Toggled Automatic Date & Time Off")

        if shutdownFlag: return
            
        # Open Date Selection Menu
        await clickScreenPositionWithDelay(settingsPositions.select_date, "Opened Date Selection Menu")

        if shutdownFlag: return
            
        # Change Day to Selected Ahead Date to Get Rewards
        await clickScreenPositionWithDelay(settingsPositions.change_day, "Changed Day to Selected Ahead Date")

        if shutdownFlag: return
            
        # Go Back to Home Menu
        await clickScreenPositionWithDelay(generalPositions.exit_bar_bottom, "Home Menu Button Clicked")

        if shutdownFlag: return
            
        # Open Idle Miner Tycoon Application
        await executionDelay(3)  # Wait for 3 seconds to ensure the app is loaded

        if shutdownFlag: return
            
        await clickScreenPositionWithDelay(appPositions.idle_miner_tycoon, "Idle Miner Tycoon Application Button Clicked", delayInSeconds=5)

        if shutdownFlag: return

        # Collect 2x Rewards Button
        await clickScreenPositionWithDelay(gamePositions.collect_2x_rewards, "Collect 2x Rewards Button Clicked")

        if shutdownFlag: return

        # Confirm Collect 2x Rewards Button
        await clickScreenPositionWithDelay(gamePositions.collect_2x_rewards_confirm, "Collect 2x Rewards Confirmed")

        if shutdownFlag: return

        # Go Back to Home Menu
        await clickScreenPositionWithDelay(generalPositions.exit_bar_bottom, "Home Menu Button Clicked")

        if shutdownFlag: return

        # NEXT CYCLE START AFTER START CYCLE
        while True:
            # Open Settings Application
            await clickScreenPositionWithDelay(appPositions.settings, "Settings Application Button Clicked")
            if shutdownFlag: return
            # Go to Settings Application Search Bar
            await clickScreenPositionWithDelay(settingsPositions.current_day, "Settings Application Current Day Clicked")
            if shutdownFlag: return
            # Go Back to Home Menu
            await clickScreenPositionWithDelay(generalPositions.exit_bar_bottom, "Home Menu Button Clicked")
            if shutdownFlag: return

            # Open Idle Miner Tycoon Application
            await asyncio.sleep(3)  # Wait for 10 seconds to ensure the app is loaded

            if shutdownFlag: return

            await clickScreenPositionWithDelay(appPositions.idle_miner_tycoon, "Idle Miner Tycoon Application Button Clicked", delayInSeconds=5)

            if shutdownFlag: return

            # Go Back to Home Menu
            await clickScreenPositionWithDelay(generalPositions.exit_bar_bottom, "Home Menu Button Clicked")
            if shutdownFlag: return
            
            # Open Settings Application
            await clickScreenPositionWithDelay(appPositions.settings, "Settings Application Button Clicked")
            if shutdownFlag: return
            
            # Change Day to Selected Ahead Date to Get Rewards
            await clickScreenPositionWithDelay(settingsPositions.change_day, "Changed Day to Selected Ahead Date")

            if shutdownFlag: return
            
            # Go Back to Home Menu
            await clickScreenPositionWithDelay(generalPositions.exit_bar_bottom, "Home Menu Button Clicked")

            if shutdownFlag: return
            # Open Idle Miner Tycoon Application
            await executionDelay(3)  # Wait for 10 seconds to ensure the app is loaded
            await clickScreenPositionWithDelay(appPositions.idle_miner_tycoon, "Idle Miner Tycoon Application Button Clicked", delayInSeconds=5)
            if shutdownFlag: return
            
            # Collect 2x Rewards Button
            await clickScreenPositionWithDelay(gamePositions.collect_2x_rewards, "Collect 2x Rewards Button Clicked")
            if shutdownFlag: return
            
            # Confirm Collect 2x Rewards Button
            await clickScreenPositionWithDelay(gamePositions.collect_2x_rewards_confirm, "Collect 2x Rewards Confirmed")
            if shutdownFlag: return
            
            # Go Back to Home Menu
            await clickScreenPositionWithDelay(generalPositions.exit_bar_bottom, "Home Menu Button Clicked")
            if shutdownFlag: return

    try:
        await automateIdleMinerTycoon()
        
        if not shutdownFlag:
            await asyncio.sleep(2)  # Wait for 2 seconds to see the effect
            
    except Exception as e:
        logging.error(f"An error occurred: {e}")
    finally:
        # Clean up
        listener.stop()
        if shutdownFlag():
            logging.info("Program shutdown completed.")
            print("Program shutdown completed.")
            sys.exit(0)

if __name__ == "__main__":
    asyncio.run(main())
