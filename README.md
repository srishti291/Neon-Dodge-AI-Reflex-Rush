# Neon-Dodge-AI-Reflex-Rush

An interactive arcade-style dodge game built with Python and Pygame, featuring dynamic difficulty levels, vibrant neon aesthetics, and adaptive AI-powered enemy mechanics.

## 🎮 Features

- **Multiple Difficulty Levels**: Choose from Easy, Medium, Hard, or Advanced modes
- **Dynamic AI Mechanics**: Enemy speed increases progressively as you survive longer
- **Vibrant Neon Design**: Eye-catching gradient backgrounds and colorful enemies
- **Score Persistence**: Automatic high score tracking saved locally
- **Smooth Gameplay**: Optimized collision detection and 30 FPS performance
- **Stylized Player Design**: Unique player character with diagonal stripes and borders

## 🎯 Gameplay

Dodge falling enemies by moving left and right. Survive as long as possible while the game becomes progressively harder. Each dodged enemy increases your score and slightly speeds up the next wave!

## 🎮 How to Play

### Controls
- **← Left Arrow**: Move player left
- **→ Right Arrow**: Move player right
- **Mouse Click**: Select difficulty level and restart game

### Gameplay Tips
- Start with Easy mode to learn the mechanics
- Watch for color changes - each enemy has a different vibrant color
- Focus on positioning - anticipate where enemies will fall
- The game gets harder over time - stay alert!

## 🛠️ Technical Details

- **Language**: Python 3.x
- **Library**: Pygame 2.5.2
- **Screen Resolution**: 800x600 pixels
- **Frame Rate**: 30 FPS
- **Color Palette**: Vibrant Red, Blue, Green, Yellow, Purple
- **Features**: Gradient rendering, collision detection, persistent storage

## 📁 Project Structure
```
Neon-Dodge-AI-Reflex-Rush/
├── neon_dodge.py          # Main game file
├── README.md              # Project documentation
├── requirements.txt       # Python dependencies
├── .gitignore            # Git ignore rules
├── LICENSE               # MIT License
└── highest_score.txt     # Generated during gameplay (stores high score)
```

## 🎨 Game Mechanics

### Difficulty Levels
| Level    | Initial Speed | Challenge |
|----------|---------------|-----------|
| Easy     | 5 units/frame | Beginner-friendly |
| Medium   | 8 units/frame | Moderate challenge |
| Hard     | 12 units/frame | Fast-paced action |
| Advanced | 16 units/frame | Expert reflexes required |

### Progressive Difficulty
- Enemy speed increases by 0.5 units per successful dodge
- Enemies spawn at random horizontal positions
- Color changes with each new enemy for visual variety

## 🏆 High Score System

Your highest score is automatically saved in `highest_score.txt` and persists across game sessions. Challenge yourself to beat your personal best!

## 📝 Future Enhancements

- [ ] Power-ups and bonus items
- [ ] Sound effects and background music
- [ ] Leaderboard with multiple player profiles
- [ ] Additional enemy types with unique behaviors
- [ ] Mobile touch controls support

## 👩‍💻 Author

**Srishti Gupta**
- GitHub: [@srishti291](https://github.com/srishti291)

## 🙏 Acknowledgments

- Built with [Pygame](https://www.pygame.org/)
- Inspired by classic arcade dodge games

## 📞 Support

If you encounter any issues or have questions, please open an issue on GitHub or contact me via email.

---

**Enjoy the game and happy dodging! 🎮✨**
