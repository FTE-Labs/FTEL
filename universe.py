from flask import Flask, render_template, render_template_string
import numpy as np

app = Flask(__name__)

# YOUR 30 CONSTANT WARHEAD (Barrow/Rees/Penrose)
constants = {
    'cosmo_constant': 1e-120, 'strong_force': 5e-3, 'gravity': 1e-3,
    'em_coupling': 3e-3, 'weak_force': 1e-2, 'Higgs_vev': 1e-34,
    'initial_entropy': 1e-10**10, 'proton_neutron': 1e-3,
    'fine_struc': 1e-4, 'em_strong_ratio': 1e-40, 'theta_QCD': 1e-10,
    'up_down_quark': 3e-5, 'alpha_s': 1e-3, 'WIMP_density': 1e-4,
    'baryon_density': 1e-10
}
for i in range(15): constants[f'param_{i}'] = 1e-25

def run_monte_carlo():
    windows = np.array(list(constants.values())[:30])
    hits = 0
    for _ in range(10**6):  # Kid-friendly speed
        trial = np.random.uniform(0, 1, 30)
        if np.all(trial < windows): hits += 1
    prob = hits / 10**6
    return prob, 1/prob if prob > 0 else float('inf')

def single_tweak_test():
    failures = 0
    for window in list(constants.values())[:30]:
        tweaked = np.random.normal(1, 0.001)
        if abs(tweaked-1) > window: failures += 1
    return failures / 30

@app.route('/')
@app.route('/universe')
def universe():
    return render_template('universe.html')

@app.route('/earth')
def earth():
    return render_template('earth.html')

@app.route('/bio')
def bio():
    return render_template('bio.html')

@app.route('/math')
def math():
    return render_template('math.html')

@app.route('/about')
def about():
    return render_template('about.html')

    
    html = """
<!DOCTYPE html>
<html>
<head>
    <title>Calibrator's Seal 🚀</title>
    <style>
        body { font-family: Arial, sans-serif; background: linear-gradient(45deg, #000011 0%, #000033 20%, #0a0a2a 40%, #1a0033 60%, #000011 100%); background-size: 600% 600%; animation: gradientShift 20s ease infinite; color: #e0e0ff; text-align: center; padding: 50px; min-height: 100vh; } }
        @keyframes gradientShift { 0% { background-position: 0% 50%; } 50% { background-position: 100% 50%; } 100% { background-position: 0% 50%; } }
        h1 { font-size: 3em; text-shadow: 2px 2px 4px rgba(0,0,0,0.5); }
        .result { background: rgba(255,255,255,0.1); padding: 20px; border-radius: 15px; margin: 20px auto; max-width: 600px; }
        .inf { font-size: 2em; color: #ff4444; font-weight: bold; }
        button { background: #ff6b35; color: white; border: none; padding: 15px 30px; font-size: 18px; border-radius: 25px; cursor: pointer; }
        button:hover { background: #e55a2b; }
        .code { background: rgba(0,0,0,0.3); padding: 20px; border-radius: 10px; font-family: monospace; max-height: 300px; overflow: auto; }
        .razor { font-size: 1.3em; margin: 20px; }
    </style>
<style>
<style>
/* TRISEUM COSMIC BACKGROUND v1 */
body { 
  margin: 0; 
  background: #0a0a1f; 
  overflow-x: hidden;
  font-family: 'Courier New', monospace;
}

.hero-section {
  height: 100vh;
  background: 
    radial-gradient(ellipse at bottom, #1a0033 0%, transparent 70%),
    radial-gradient(ellipse at top, #ff00ff20 0%, transparent 70%),
    linear-gradient(45deg, #0a0a2a 0%, #1a0033 50%, #2a0e5a 100%);
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
}

.hero-section::before {
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0; bottom: 0;
  background-image: 
    radial-gradient(circle at 20% 80%, #00ff8820 0%, transparent 50%),
    radial-gradient(circle at 80% 20%, #ffaa0020 0%, transparent 50%),
    radial-gradient(circle at 40% 40%, #8a2be220 0%, transparent 50%);
  animation: particleFloat 20s infinite linear;
}

@keyframes particleFloat {
  0%, 100% { transform: translateY(0px) scale(1); }
  50% { transform: translateY(-20px) scale(1.1); }
}

.hero-title {
  text-align: center;
  color: #00ff88;
  text-shadow: 0 0 30px #00ff88;
  z-index: 10;
  animation: glow 3s ease-in-out infinite alternate;
}

@keyframes glow {
  from { text-shadow: 0 0 20px #00ff88, 0 0 30px #00ff88; }
  to { text-shadow: 0 0 30px #00ff88, 0 0 50px #00ff88, 0 0 60px #00ff88; }
}

.calibrator-card {
  margin: 40px auto;
  max-width: 900px;
  padding: 20px;
  border-radius: 20px;
  box-shadow: 0 20px 40px rgba(0,0,0,0.5);
  transition: transform 0.3s ease;
}
.calibrator-card:hover {
  transform: translateY(-10px);
}


/* FTEL SPACESHIP NAVIGATION */
.ftel-nav {
    background: rgba(0, 0, 0, 0.9);
    backdrop-filter: blur(20px);
    border-bottom: 2px solid #00bfff;
    position: sticky;
    top: 0;
    z-index: 1000;
    box-shadow: 0 4px 20px rgba(0, 191, 255, 0.3);
}

.nav-container {
    max-width: 1200px;
    margin: 0 auto;
    display: flex;
    justify-content: center;
    gap: 0;
}

.nav-link {
    color: #00bfff !important;
    text-decoration: none;
    padding: 15px 25px;
    font-family: 'Courier New', monospace;
    font-weight: 900;
    font-size: 16px;
    text-transform: uppercase;
    letter-spacing: 2px;
    position: relative;
    transition: all 0.3s ease;
    text-shadow: 0 0 10px rgba(0, 191, 255, 0.5);
}

.nav-link:hover {
    background: linear-gradient(90deg, #00bfff, #1e90ff);
    color: white !important;
    box-shadow: 0 0 20px rgba(0, 191, 255, 0.6);
    transform: translateY(-2px);
}

.nav-link.active {
    background: linear-gradient(90deg, #00bfff, #1e90ff);
    color: white !important;
    box-shadow: 0 0 25px rgba(0, 191, 255, 0.8);
}

/* MOBILE RESPONSIVE */
@media (max-width: 768px) {
    .nav-container {
        flex-direction: column;
        gap: 0;
    }
    .nav-link {
        padding: 12px 20px;
        font-size: 14px;
        border-bottom: 1px solid rgba(0, 191, 255, 0.3);
    }
}


</style>
</head>
<body>
<!-- FTEL TOP NAVIGATION -->
<nav class="ftel-nav">
    <div class="nav-container">
        <a href="universe.html" class="nav-link active">🌌 Universe</a>
        <a href="earth.html" class="nav-link">🌍 Earth</a>
        <a href="bio.html" class="nav-link">🧬 Bio</a>
        <a href="math.html" class="nav-link">🧮 Math</a>
        <a href="about.html" class="nav-link">ℹ️ About</a>
    </div>
</nav>



<!-- 🌌 MILKY WAY HERO - WORKING -->
<style>
.hero-section {
  height: 100vh;
  background-image: url('https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=2070&auto=format&fit=crop&q=80');
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  background-attachment: fixed;
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
}
.hero-section::before {
  content: '';
  position: absolute; top: 0; left: 0; right: 0; bottom: 0;
  background: rgba(10,10,40,0.65);
}
.hero-title {
  text-align: center;
  color: #00ff88;
  font-family: monospace;
  text-shadow: 0 0 40px #00ff88;
  z-index: 10;
}
</style>

<div class="hero-section">
  <div class="hero-title">
    <!-- BLUE CALCULATOR FONT VERSION (KEEP THIS) -->
    <h1 style="font-family: 'Courier New', 'LCDMono', monospace; font-size: 6vw; margin: 0; letter-spacing: 8px; color: #00bfff; text-shadow: 0 0 20px rgba(0,191,255,0.8); font-weight: 900;">FINE TUNING ENGINEERING LABS</h1>
    
    <!-- YELLOW BACKUP VERSION (DELETE LATER) -->
    <!-- <h1 style="font-family: 'Courier New', monospace; font-size: 6vw; margin: 0; letter-spacing: 8px; color: #ffaa00; text-shadow: 0 0 30px #ffaa00; font-weight: 900;">FINE TUNING ENGINEERING LABS</h1> -->
    
    <h2 style="font-size: 3vw; color: #ffaa00; margin: 20px 0; text-shadow: 0 0 30px #ffaa00;">RISER100W-BINARYRAINBOW</h2>
    <p style="font-size: 1.8vw; color: white;">Cosmic Calibrators Online</p>
  </div>
</div>


<div style="max-width: 1200px; margin: 0 auto; padding: 20px;">
<div class="calib-box" style="background: #ffffff; margin: 30px 0; padding: 25px; border-radius: 15px; box-shadow: 0 10px 30px rgba(0,0,0,0.1);">
    <h2 style="color: #00bfff; text-align: center;">🎯 10-CONSTANT FINE-TUNING</h2>
<p style="color: #1e3a8a !important; text-align: center; font-size: 16px; margin: 10px 0 20px 0; font-style: italic; font-weight: 500;">
<strong>Challenge:</strong> Can 10 constants hit the exact range where stars form, planets stabilize AND life becomes possible - ALL AT ONCE, via Random Chaos?
 Probability = insane. 🌌⚛️<</p>

    
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px; margin: 20px 0;">
        <!-- Λ cosmo -->
        <label style="display: flex; align-items: center; gap: 10px; cursor: pointer;">
            <span style="color: #00bfff; font-weight: bold; font-size: 14px; min-width: 70px;">Λ cosmo</span>
            <div class="toggle-switch" data-id="1" data-win="1e-120"><span class="toggle-circle"></span></div>
        </label>
        
        <!-- Strong -->
        <label style="display: flex; align-items: center; gap: 10px; cursor: pointer;">
            <span style="color: #00bfff; font-weight: bold; font-size: 14px; min-width: 70px;">Strong</span>
            <div class="toggle-switch" data-id="2" data-win="0.005"><span class="toggle-circle"></span></div>
        </label>
        
        <!-- Gravity -->
        <label style="display: flex; align-items: center; gap: 10px; cursor: pointer;">
            <span style="color: #00bfff; font-weight: bold; font-size: 14px; min-width: 70px;">Gravity</span>
            <div class="toggle-switch" data-id="3" data-win="0.001"><span class="toggle-circle"></span></div>
        </label>
      
        <!-- EM α -->
        <label style="display: flex; align-items: center; gap: 10px; cursor: pointer;">
            <span style="color: #00bfff; font-weight: bold; font-size: 14px; min-width: 70px;">EM α</span>
            <div class="toggle-switch" data-id="4" data-win="0.003"><span class="toggle-circle"></span></div>
        </label>
       
        <!-- Weak -->
        <label style="display: flex; align-items: center; gap: 10px; cursor: pointer;">
            <span style="color: #00bfff; font-weight: bold; font-size: 14px; min-width: 70px;">Weak</span>
            <div class="toggle-switch" data-id="5" data-win="0.01"><span class="toggle-circle"></span></div>
        </label>
       
        <!-- Higgs -->
        <label style="display: flex; align-items: center; gap: 10px; cursor: pointer;">
            <span style="color: #00bfff; font-weight: bold; font-size: 14px; min-width: 70px;">Higgs</span>
            <div class="toggle-switch" data-id="6" data-win="0.002"><span class="toggle-circle"></span></div>
        </label>
       
        <!-- e-mass -->
        <label style="display: flex; align-items: center; gap: 10px; cursor: pointer;">
            <span style="color: #00bfff; font-weight: bold; font-size: 14px; min-width: 70px;">e-mass</span>
            <div class="toggle-switch" data-id="7" data-win="0.0001"><span class="toggle-circle"></span></div>
        </label>
       
        <!-- u/d quark -->
        <label style="display: flex; align-items: center; gap: 10px; cursor: pointer;">
            <span style="color: #00bfff; font-weight: bold; font-size: 14px; min-width: 70px;">u/d quark</span>
            <div class="toggle-switch" data-id="8" data-win="0.0005"><span class="toggle-circle"></span></div>
        </label>
       
        <!-- Entropy -->
        <label style="display: flex; align-items: center; gap: 10px; cursor: pointer;">
            <span style="color: #00bfff; font-weight: bold; font-size: 14px; min-width: 70px;">Entropy</span>
            <div class="toggle-switch" data-id="9" data-win="1e-10"><span class="toggle-circle"></span></div>
        </label>
       
        <!-- Density -->
        <label style="display: flex; align-items: center; gap: 10px; cursor: pointer;">
            <span style="color: #00bfff; font-weight: bold; font-size: 14px; min-width: 70px;">Density</span>
            <div class="toggle-switch" data-id="10" data-win="1e-60"><span class="toggle-circle"></span></div>
        </label>
</div>

    
    <button id="resetBtn" style="width: 100%; padding: 12px; background: linear-gradient(45deg, #00bfff, #1e90ff); color: white; border: none; border-radius: 25px; font-size: 16px; font-weight: bold; cursor: pointer;">🔄 RESET ALL</button>
    
<div id="resultBox" style="background: #f8f9ff; color: #000; padding: 25px; border-radius: 15px; border: 2px solid #00bfff; font-size: 20px; text-align: center; margin-top: 20px; display: none;">
    <div id="computing" style="font-size: 24px; color: #00bfff;">⚙️ COMPUTING...</div>
    <div id="finalResult" style="display: none;">
        Life-permitting: <span id="probProd">1.000</span><br>
        1 in 10<sup id="totalExp">0</sup><br>
        (<span id="winCount">0</span> constants)
    </div>
</div>

<!-- LOTTERY COMPARISON BOX -->
<div id="lotteryBox" style="background: linear-gradient(135deg, #4fc3f7, #0288d1); color: white; padding: 25px; border-radius: 15px; margin-top: 15px; display: none; box-shadow: 0 10px 30px rgba(255,68,68,0.4); border: 2px solid #ff6666;">
    <div style="font-size: 22px; font-weight: bold; margin-bottom: 10px;">🎰 LOTTERY EQUIVALENT</div>
    <div style="font-size: 28px; text-shadow: 0 0 10px rgba(255,255,255,0.5);">
        <span id="lotteryWins">0</span> Powerball jackpots in a row!
    </div>
    <div style="font-size: 14px; opacity: 0.9; margin-top: 8px;">(1 in 292 million per ticket)</div>
</div>

<style>

.toggle-switch {
    position: relative; width: 55px; height: 28px; background: #ddd; border-radius: 14px;
    transition: all 0.3s ease; cursor: pointer; box-shadow: inset 0 2px 4px rgba(0,0,0,0.1);
}
.toggle-switch.active {
    background: linear-gradient(90deg, #00bfff, #1e90ff); box-shadow: 0 0 12px rgba(0,191,255,0.4);
}
.toggle-circle {
    position: absolute; top: 2px; left: 2px; width: 24px; height: 24px;
    background: #fff; border-radius: 50%; transition: transform 0.3s ease;
    box-shadow: 0 2px 6px rgba(0,0,0,0.2);
}
.toggle-switch.active .toggle-circle { transform: translateX(27px); }
</style>

<script>
let selectedWins = [];

document.querySelectorAll('.toggle-switch').forEach(toggle => {
    toggle.addEventListener('click', function() {
        this.classList.toggle('active');
        let id = parseInt(this.dataset.id);
        let winSize = parseFloat(this.dataset.win);
        
        let idx = selectedWins.findIndex(w => w.id === id);
        if (idx > -1) {
            selectedWins.splice(idx, 1);
        } else {
            selectedWins.push({id: id, window: winSize});
        }
        computeLive();
    });
});

function computeLive() {
    document.getElementById('computing').style.display = 'block';
    document.getElementById('finalResult').style.display = 'none';
    document.getElementById('resultBox').style.display = 'block';
    
    setTimeout(() => {
        let prod = 1.0;
        selectedWins.forEach(w => prod *= w.window);
        let odds = 1 / prod;
        let exp = Math.round(Math.log10(odds));

        document.getElementById('computing').style.display = 'none';
        document.getElementById('finalResult').style.display = 'block';
        document.getElementById('probProd').innerHTML = prod.toExponential(3);
        document.getElementById('totalExp').innerHTML = exp;
        document.getElementById('winCount').innerHTML = selectedWins.length;

        // LOTTERY MAGIC
        let powerballDigits = 8.46;
        let lotteryWins = Math.max(0, Math.floor(exp / powerballDigits));
        document.getElementById('lotteryBox').style.display = 'block';
        document.getElementById('lotteryWins').innerHTML = lotteryWins.toLocaleString();
    }, 600);
}

document.getElementById('resetBtn').addEventListener('click', function() {
    selectedWins = [];
    document.querySelectorAll('.toggle-switch').forEach(toggle => {
        toggle.classList.remove('active');
    });
    document.getElementById('resultBox').style.display = 'none';
    document.getElementById('lotteryBox').style.display = 'none';
});
</script>
</div>

<!-- SLIDER CHAOS v3.3 - LIMIT MARKS -->
<div id="chaos-section" style="background: #ffffff; padding: 25px; border-radius: 15px; margin: 20px 0; box-shadow: 0 10px 30px rgba(0,0,0,0.1); border: 1px solid #e0e0e0; position: relative;">
    <h3 style="color: #00bfff; text-align: center; margin: 0 0 20px 0; font-size: 24px;">💥 SLIDER CHAOS v3.3</h3>
<p style="color: #1e3a8a !important; text-align: center; font-size: 16px; margin: 10px 0 20px 0; font-style: italic; font-weight: 500;">
<strong>Test:</strong> One tiny slider nudge crashes stars OR explodes the universe. How precise does physics need to be? 💥⚖️</p>
    
    
    <div style="margin-bottom: 40px;">
        <label style="display: block; color: #00bfff; font-weight: bold; margin-bottom: 8px;">Strong Force</label>
        <input type="range" id="s" min="0.99" max="1.01" step="0.0001" value="1" class="chaos-slider">
        <span id="sd" style="color: #666; font-family: monospace; font-size: 16px;">1.000</span>
    </div>
    
    <div>
        <label style="display: block; color: #00bfff; font-weight: bold; margin-bottom: 8px;">Gravity</label>
        <input type="range" id="g" min="0.98" max="1.02" step="0.0001" value="1" class="chaos-slider">
        <span id="gd" style="color: #666; font-family: monospace; font-size: 16px;">1.000</span>
    </div>
    
    <button onclick="resetChaos()" style="width: 100%; padding: 12px; background: linear-gradient(45deg, #00bfff, #1e90ff); color: white; border: none; border-radius: 25px; font-size: 16px; font-weight: bold; cursor: pointer; margin: 20px 0;">🔄 CHAOS RESET</button>
    
    <div id="out" style="background: linear-gradient(135deg, #f8f9ff, #e6f3ff); color: #333; padding: 20px; border-radius: 15px; font-weight: bold; text-align: center; border: 2px solid #00bfff; font-size: 18px;">UNIVERSE OK</div>
</div>

<style>
/* COMPACT WIDE SLIDERS WITH LIMIT MARKS */
.chaos-slider {
    -webkit-appearance: none;
    appearance: none;
    width: 280px; /* Narrower than 100% */
    height: 12px;
    border-radius: 6px;
    background: #e8f4ff;
    outline: none;
    box-shadow: inset 0 2px 4px rgba(0,0,0,0.1);
}

.chaos-slider::-webkit-slider-thumb {
    -webkit-appearance: none;
    width: 28px;
    height: 28px;
    background: #00bfff;
    border-radius: 4px; /* Square with tiny corners */
    cursor: pointer;
    box-shadow: 0 4px 12px rgba(0,191,255,0.4);
    border: 2px solid #ffffff;
    margin-top: -8px;
}

.chaos-slider::-moz-range-thumb {
    width: 28px;
    height: 28px;
    background: #00bfff;
    border-radius: 4px;
    cursor: pointer;
    box-shadow: 0 4px 12px rgba(0,191,255,0.4);
    border: 2px solid #ffffff;
    border: none;
}
</style>

<!-- SAME SCRIPT - NO CHANGES NEEDED -->
<script>
let chaosReady = false;

function c(){
    let s=document.getElementById('s').value;
    let g=document.getElementById('g').value;
    document.getElementById('sd').innerHTML=s;
    document.getElementById('gd').innerHTML=g;
    let o=document.getElementById('out');
    if(s<0.995){
        o.innerHTML='NO STARS!';o.style.color='#f00';
    } else if(s>1.005){
        o.innerHTML='NO CHEMISTRY!';o.style.color='#f80';
    } else if(g<0.99){
        o.innerHTML='NO GALAXIES!';o.style.color='#f00';
    } else if(g>1.01){
        o.innerHTML='BIG CRUNCH!';o.style.color='#f00';
    } else {
        o.innerHTML='UNIVERSE OK';o.style.color='#333';
    }
}

function resetChaos() {
    document.getElementById('s').value = 1;
    document.getElementById('g').value = 1;
    c();
}

document.addEventListener('DOMContentLoaded', function(){
    if(!chaosReady){
        document.getElementById('s').oninput=c;
        document.getElementById('g').oninput=c;
        c();
        chaosReady = true;
    }
});
</script>

<script>
let chaosReady = false;

function c(){
    let s=document.getElementById('s').value;
    let g=document.getElementById('g').value;
    document.getElementById('sd').innerHTML=s;
    document.getElementById('gd').innerHTML=g;
    let o=document.getElementById('out');
    if(s<0.995){
        o.innerHTML='NO STARS!';o.style.color='#f00';
    } else if(s>1.005){
        o.innerHTML='NO CHEMISTRY!';o.style.color='#f80';
    } else if(g<0.99){
        o.innerHTML='NO GALAXIES!';o.style.color='#f00';
    } else if(g>1.01){
        o.innerHTML='BIG CRUNCH!';o.style.color='#f00';
    } else {
        o.innerHTML='UNIVERSE OK';o.style.color='#333';
    }
}

function resetChaos() {
    document.getElementById('s').value = 1;
    document.getElementById('g').value = 1;
    c();
}

document.addEventListener('DOMContentLoaded', function(){
    if(!chaosReady){
        document.getElementById('s').oninput=c;
        document.getElementById('g').oninput=c;
        c();
        chaosReady = true;
    }
});
</script>

<!-- HYPERCUBE v4.0 - SPACESHIP EDITION -->
<div style="background: #ffffff; padding: 25px; border-radius: 15px; margin: 30px 0; box-shadow: 0 10px 30px rgba(0,0,0,0.1); border: 1px solid #e0e0e0; position: relative;">
    <h2 style="color: #00bfff; text-align: center; margin: 0 0 20px 0; font-size: 24px;">🌀 HYPERCUBE (10D)</h2>
<p style="color: #1e3a8a !important; text-align: center; font-size: 16px; margin: 10px 0 20px 0; font-style: italic; font-weight: 500;">
    <strong>Math:</strong> Fine-structure constant (1/137) must be exact or atoms won't form. Change by 4% = lifeless cosmos. 🌀🔢</p>

    
    <div style="margin-bottom: 35px;">
        <label style="display: block; color: #00bfff; font-weight: bold; margin-bottom: 8px;">Alpha (EM Fine Structure)</label>
        <input type="range" id="HA" min="0.007" max="0.008" step="0.00001" value="0.007297" class="hyper-slider">
        <span id="DA" style="color: #666; font-family: monospace; font-size: 16px;">0.0073</span>
    </div>
    
    <div style="margin-bottom: 35px;">
        <label style="display: block; color: #00bfff; font-weight: bold; margin-bottom: 8px;">Strong Force</label>
        <input type="range" id="HS" min="0.99" max="1.01" step="0.001" value="1" class="hyper-slider">
        <span id="DS" style="color: #666; font-family: monospace; font-size: 16px;">1.000</span>
    </div>
    
    <div>
        <label style="display: block; color: #00bfff; font-weight: bold; margin-bottom: 8px;">Gravity</label>
        <input type="range" id="HG" min="0.98" max="1.02" step="0.001" value="1" class="hyper-slider">
        <span id="DG" style="color: #666; font-family: monospace; font-size: 16px;">1.000</span>
    </div>
    
    <button onclick="resetHypercube()" style="width: 100%; padding: 12px; background: linear-gradient(45deg, #00bfff, #1e90ff); color: white; border: none; border-radius: 25px; font-size: 16px; font-weight: bold; cursor: pointer; margin: 20px 0;">🔄 HYPERCUBE RESET</button>
    
    <div id="HC_STATUS" style="background: linear-gradient(135deg, #f8f9ff, #e6f3ff); color: #333; padding: 20px; border-radius: 15px; text-align: center; font-size: 22px; font-weight: bold; border: 2px solid #00bfff;">🌀 10D STABLE</div>
</div>

<style>
/* HYPERCUBE SQUARE SLIDERS */
.hyper-slider {
    -webkit-appearance: none;
    appearance: none;
    width: 280px; /* Perfect width */
    height: 12px;
    border-radius: 6px;
    background: #e8f4ff;
    outline: none;
    box-shadow: inset 0 2px 4px rgba(0,0,0,0.1);
}

.hyper-slider::-webkit-slider-thumb {
    -webkit-appearance: none;
    width: 28px;
    height: 28px;
    background: #00bfff;
    border-radius: 4px; /* Square with tiny round */
    cursor: pointer;
    box-shadow: 0 4px 12px rgba(0,191,255,0.4);
    border: 2px solid #ffffff;
    margin-top: -8px;
}

.hyper-slider::-moz-range-thumb {
    width: 28px;
    height: 28px;
    background: #00bfff;
    border-radius: 4px;
    cursor: pointer;
    box-shadow: 0 4px 12px rgba(0,191,255,0.4);
    border: 2px solid #ffffff;
    border: none;
}
</style>

<!-- SAME FUNCTIONALITY - NO SCRIPT CHANGES -->
<script>
function checkHyper() {
    let a = +document.getElementById('HA').value;
    let s = +document.getElementById('HS').value;
    let g = +document.getElementById('HG').value;
document.getElementById('DA').innerHTML = a.toFixed(4);
    document.getElementById('DS').innerHTML = s.toFixed(3);
    document.getElementById('DG').innerHTML = g.toFixed(3);
    
    let alive = (a <= 0.007397) && (s >= 0.995 && s <= 1.005) && (Math.abs(g - 1.0) <= 0.015);
    
    let status = document.getElementById('HC_STATUS');
    if (alive) {
        status.innerHTML = '🌀 10D STABLE';
        status.style.color = '#333';
        status.style.borderColor = '#00bfff';
    } else {
        status.innerHTML = '💀 10D DEAD';
        status.style.color = '#f00';
        status.style.borderColor = '#f00';
    }
}

function resetHypercube() {
    document.getElementById('HA').value = 0.007297;
    document.getElementById('HS').value = 1;
    document.getElementById('HG').value = 1;
    checkHyper();
}

document.addEventListener('DOMContentLoaded', function(){
    document.getElementById('HA').oninput = checkHyper;
    document.getElementById('HS').oninput = checkHyper;
    document.getElementById('HG').oninput = checkHyper;
    checkHyper();
});
</script>

<!-- MASTER RESET CONTROL PANEL v9.2 - SPACESHIP EDITION -->
<div style="background: #ffffff; padding: 25px; border-radius: 15px; margin: 30px 0; text-align: center; box-shadow: 0 10px 30px rgba(0,0,0,0.1); border: 1px solid #e0e0e0;">
    <h2 style="color: #00bfff; font-size: 24px; margin: 0 0 20px 0; text-shadow: 0 0 10px rgba(0,191,255,0.5);">💥 MASTER CONTROL PANEL v9.2</h2>
    
    <button onclick="masterResetAll()" style="width: 100%; padding: 18px 30px; background: linear-gradient(45deg, #00bfff, #1e90ff); color: white; border: none; border-radius: 30px; font-size: 20px; font-weight: 900; cursor: pointer; box-shadow: 0 8px 25px rgba(0,191,255,0.4); transition: all 0.3s ease; font-family: 'Courier New', monospace; text-transform: uppercase; letter-spacing: 2px;">
        🔥 MASTER RESET ALL SECTIONS
    </button>
    
    <div style="margin-top: 15px; padding: 12px; background: linear-gradient(135deg, #f8f9ff, #e6f3ff); border-radius: 10px; border: 2px solid #00bfff; font-size: 14px; color: #666; font-family: monospace;">
        Resets: Constants • Chaos • Hypercube • Multiverse
    </div>
</div>

<script>
function masterResetAll() {
    // CHAOS SLIDERS
    if(document.getElementById('s')) {
        document.getElementById('s').value = 1;
        document.getElementById('g').value = 1;
        if(typeof c === 'function') c();
    }
    
    // HYPERCUBE
    if(document.getElementById('HA')) {
        document.getElementById('HA').value = 0.007297;
        document.getElementById('HS').value = 1;
        document.getElementById('HG').value = 1;
        if(typeof checkHyper === 'function') checkHyper();
    }
    

// 10-CONSTANT TOGGLES (FORCE GLOBAL)
if(typeof resetAll === 'function') {
    resetAll();
} else {
    // MANUAL RESET as backup
    selectedWins = [];
    document.querySelectorAll('.toggle-switch')?.forEach(toggle => {
        toggle.classList.remove('active');
    });
    const resultBoxes = document.querySelectorAll('#resultBox, #lotteryBox');
    resultBoxes.forEach(box => box.style.display = 'none');
}

    
    // MULTIVERSE (if exists)
    if(document.getElementById('uniSlide')) {
        document.getElementById('uniSlide').value = 6;
        if(document.getElementById('uniDisplay')) {
            document.getElementById('uniDisplay').innerText = 'Universe #6 / 12 Dimensions Active';
        }
    }
    
    // HIDE ALL RESULT BOXES
    const resultBoxes = document.querySelectorAll('#resultBox, #lotteryBox');
    resultBoxes.forEach(box => box.style.display = 'none');
}
</script>
</div>
</body>
</html>
    """
    return render_template_string(html, prob=prob, odds=odds, failure_rate=failure_rate, 
                                code=open(__file__).read())

if __name__ == '__main__':
    import sys
    port = 5001
    if len(sys.argv) > 1:
        port = int(sys.argv[1].replace('-p', ''))
    app.run(host='0.0.0.0', port=port, debug=True)

    
