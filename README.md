# Smart Gym AI - Professional Fitness Tracker

An AI-powered fitness application that provides real-time pose detection and rep counting for multiple exercises. Built with modern web technologies for cross-platform compatibility.

## ✨ Features

- **Real-time Pose Detection**: Uses MediaPipe AI for accurate body tracking
- **Multiple Exercises**: Support for 6 different exercises
  - 💪 Bicep Curl
  - 🏃 Squat
  - 🤸 Push-up
  - 🏋️ Shoulder Press
  - 🦵 Lunge
  - 🧘 Plank
- **Professional UI**: Modern, responsive design that works on all devices
- **Live Tracking**: Real-time rep counting, stage detection, and timer
- **Progress Visualization**: Visual progress bars and workout summaries
- **Voice Commands**: Hands-free control with speech recognition and audio feedback
- **Mobile Compatible**: Works on phones, tablets, and desktops
- **No Installation Required**: Pure web application

## 🎨 Design Features

- **Modern Glassmorphism**: Backdrop blur effects and transparent elements
- **Smooth Animations**: CSS transitions and keyframe animations
- **Responsive Layout**: Adapts perfectly to any screen size
- **Professional Typography**: Inter font with proper hierarchy
- **Gradient Backgrounds**: Beautiful color schemes throughout
- **Interactive Elements**: Hover effects and micro-interactions
- **Loading States**: Professional loading overlays and status messages
- **Accessibility**: ARIA labels and semantic HTML structure

## 🎯 Supported Exercises

### Bicep Curl
Tracks left arm curls with proper form detection.

### Squat
Monitors squat depth and form using leg angles.

### Push-up
Detects push-up movement and counts reps.

### Shoulder Press
Tracks overhead press movements.

### Lunge
Monitors lunge depth and balance.

### Plank
Tracks plank hold duration (counts as reps).

## 🚀 How to Use

1. **Open the App**: Simply open `index.html` in any modern web browser
2. **Allow Camera**: Grant camera permissions when prompted
3. **Select Exercise**: Choose your workout from the dropdown
4. **Start Workout**: Click "Start Workout" and begin exercising
5. **Track Progress**: Watch real-time feedback and progress
6. **Complete Workout**: Stop when done to see your summary

## 🛠️ Technologies Used

- **MediaPipe**: AI-powered pose detection
- **HTML5/CSS3**: Modern web design with glassmorphism
- **JavaScript**: Client-side logic with async/await
- **Web Speech API**: Voice synthesis and recognition
- **Canvas API**: Real-time video overlay
- **WebRTC**: Camera access
- **CSS Grid/Flexbox**: Responsive layouts
- **CSS Animations**: Smooth transitions and effects

## 🎯 Professional Features

- **Loading States**: Elegant loading overlays during initialization
- **Status Messages**: Toast notifications for user feedback
- **Error Handling**: Graceful error messages and recovery
- **Accessibility**: Screen reader support and keyboard navigation
- **Performance**: Optimized animations and efficient rendering
- **User Experience**: Intuitive workflows and visual feedback
- **Brand Consistency**: Cohesive design language throughout

## 📱 Cross-Platform Support

This web application works on:
- **Desktop**: Chrome, Firefox, Safari, Edge
- **Mobile**: iOS Safari, Android Chrome
- **Tablets**: iPad, Android tablets

No app store installation required - just open in your browser!

## �️ **Voice Commands**

The app includes advanced voice control features for hands-free operation:

### **Voice Toggle**
- Check the "Voice Commands" box in the sidebar to enable/disable voice features
- Voice commands are only available in supported browsers (Chrome, Edge, Safari)

### **Voice Feedback**
- **Rep Announcements**: "Rep 1", "Rep 2", etc. when completing exercises
- **Stage Updates**: "Up", "Down" for movement phases
- **Workout Status**: Audio confirmations for start/stop actions

### **Voice Commands You Can Use**
- **"Start workout"** - Begins the exercise session
- **"Stop workout"** - Ends the current session
- **"Change to [exercise]"** - Switch exercises (e.g., "change to squats", "change to push-ups")
- **"How many reps?"** - Hear current rep count
- **"What stage?"** - Current movement phase
- **"Time?"** or **"How long?"** - Current workout duration

### **Voice Command Examples**
```
"Start workout"
"Stop workout"
"Change to squats"
"Change to bicep curl"
"How many reps?"
"What stage?"
"Time?"
```

### **Browser Compatibility**
- ✅ **Chrome/Edge**: Full voice support
- ✅ **Safari**: Full voice support
- ❌ **Firefox**: Limited support (speech synthesis only)
- ❌ **Mobile browsers**: May have restrictions

Voice commands work continuously during workouts for a truly hands-free experience!

## 🔧 Development

The app uses MediaPipe.js for browser-based pose detection, eliminating the need for Python backend and enabling true cross-platform compatibility.

## 📈 Future Enhancements

- Calorie burn estimation
- Workout history tracking
- Personalized form tips
- Multi-person detection
- Exercise tutorials
- Social sharing features

## 📄 License

This project is open source and available under the MIT License.
