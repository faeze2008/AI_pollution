"""
Factory Pollution Analysis System
"""

import tkinter as tk
from tkinter import ttk, messagebox
import math
from datetime import datetime

class AdvancedFactoryAnalyzer:
    def __init__(self, master):
        self.master = master
        master.title("Industrial Environmental Analysis Platform")
        master.geometry("950x800")
        master.configure(bg='#f5f7fa')
        
        
        main_container = tk.Frame(master, bg='#f5f7fa')
        main_container.pack(fill='both', expand=True, padx=20, pady=20)
        
        
        header_frame = tk.Frame(main_container, bg='#2c3e50', height=100)
        header_frame.pack(fill='x', pady=(0, 20))
        header_frame.pack_propagate(False)
        
        tk.Label(header_frame, text="INDUSTRIAL ENVIRONMENTAL ANALYSIS SYSTEM", 
                font=('Segoe UI', 18, 'bold'), bg='#2c3e50', fg='white').pack(expand=True)
        tk.Label(header_frame, text="Comprehensive Pollution Assessment & Mitigation Platform", 
                font=('Segoe UI', 10), bg='#2c3e50', fg='#ecf0f1').pack()
        
        
        content_frame = tk.Frame(main_container, bg='#f5f7fa')
        content_frame.pack(fill='both', expand=True)
        
        
        left_panel = tk.Frame(content_frame, bg='white', relief='solid', bd=1)
        left_panel.pack(side='left', fill='both', expand=True, padx=(0, 10))
        
        input_title = tk.Label(left_panel, text="OPERATIONAL PARAMETERS", 
                              font=('Segoe UI', 12, 'bold'), bg='#34495e', fg='white', 
                              padx=15, pady=10)
        input_title.pack(fill='x')
        
        
        self.parameters = [
            ("Production Volume (tons/day)", "production", 0, 10000),
            ("Furnace Temperature (°C)", "temperature", 0, 2000),
            ("Fuel Consumption (liters)", "fuel", 0, 5000),
            ("Material Quality Index", "quality", 0, 100),
            ("Process Efficiency (%)", "efficiency", 0, 100),
            ("Operating Hours", "hours", 0, 24),
            ("Equipment Age (years)", "age", 0, 50),
            ("Staff Experience Level", "experience", 1, 10),
            ("Maintenance Status", "maintenance", 0, 1),
            ("Ambient Humidity (%)", "humidity", 0, 100)
        ]
        
        self.entries = {}
        
        
        for i, (label, key, min_val, max_val) in enumerate(self.parameters):
            frame = tk.Frame(left_panel, bg='white')
            frame.pack(fill='x', padx=15, pady=8)
            
            tk.Label(frame, text=label + ":", bg='white', font=('Segoe UI', 9), 
                    width=25, anchor='w').pack(side='left')
            
            entry = tk.Entry(frame, width=15, font=('Consolas', 9), 
                           justify='right', bg='#f8f9fa')
            entry.pack(side='left', padx=5)
            entry.insert(0, "")
            
            
            entry.bind('<Return>', lambda e, idx=i: self.navigate_fields(idx, 1))
            entry.bind('<Up>', lambda e, idx=i: self.navigate_fields(idx, -1))
            entry.bind('<Down>', lambda e, idx=i: self.navigate_fields(idx, 1))
            
            self.entries[key] = entry
        
        
        button_frame = tk.Frame(left_panel, bg='white')
        button_frame.pack(fill='x', padx=15, pady=20)
        
        tk.Button(button_frame, text="Clear All", command=self.clear_all,
                 bg='#95a5a6', fg='white', font=('Segoe UI', 9), 
                 padx=15, pady=5).pack(side='left', padx=5)
        
        self.analyze_btn = tk.Button(button_frame, text="Run Environmental Analysis", 
                                    command=self.analyze_environment,
                                    bg='#27ae60', fg='white', font=('Segoe UI', 10, 'bold'),
                                    padx=20, pady=8)
        self.analyze_btn.pack(side='left', padx=5)
        
        tk.Button(button_frame, text="Export Report", command=self.export_report,
                 bg='#3498db', fg='white', font=('Segoe UI', 9),
                 padx=15, pady=5).pack(side='left', padx=5)
        
        
        right_panel = tk.Frame(content_frame, bg='white', relief='solid', bd=1)
        right_panel.pack(side='right', fill='both', expand=True)
        
        results_title = tk.Label(right_panel, text="ANALYSIS RESULTS", 
                                font=('Segoe UI', 12, 'bold'), bg='#2c3e50', fg='white', 
                                padx=15, pady=10)
        results_title.pack(fill='x')
        
        
        self.results = {
            "PM2.5 Concentration": tk.StringVar(value="-- μg/m³"),
            "SO₂ Emissions": tk.StringVar(value="-- ppm"),
            "NOx Levels": tk.StringVar(value="-- ppm"),
            "CO Output": tk.StringVar(value="-- ppm"),
            "Overall Air Quality": tk.StringVar(value="-- AQI")
        }
        
        for pollutant, var in self.results.items():
            result_frame = tk.Frame(right_panel, bg='white')
            result_frame.pack(fill='x', padx=15, pady=6)
            
            tk.Label(result_frame, text=pollutant + ":", bg='white', 
                    font=('Segoe UI', 9), width=20, anchor='w').pack(side='left')
            
            tk.Label(result_frame, textvariable=var, bg='#ecf0f1', 
                    font=('Consolas', 9), width=15, relief='solid',
                    anchor='center').pack(side='left', padx=5)
        
        #
        risk_frame = tk.Frame(right_panel, bg='white', pady=15)
        risk_frame.pack(fill='x', padx=15, pady=10)
        
        self.risk_label = tk.Label(risk_frame, text="RISK LEVEL: --", 
                                  font=('Segoe UI', 11, 'bold'), bg='white')
        self.risk_label.pack()
        
        # GAN
        rec_title = tk.Label(right_panel, text="ADVANCED MITIGATION STRATEGIES", 
                            font=('Segoe UI', 11, 'bold'), bg='#34495e', fg='white',
                            padx=15, pady=8)
        rec_title.pack(fill='x', pady=(20, 10))
        
        
        self.rec_text = tk.Text(right_panel, height=12, width=50, 
                               font=('Segoe UI', 9), wrap='word',
                               bg='#f8f9fa', relief='solid', bd=1)
        self.rec_text.pack(fill='both', expand=True, padx=15, pady=(0, 15))
        
        
        self.status = tk.Label(master, text="System Ready | Enter operational parameters above", 
                              bg='#2c3e50', fg='white', anchor='w',
                              font=('Segoe UI', 9), padx=15, pady=8)
        self.status.pack(side='bottom', fill='x')
        
        
        list(self.entries.values())[0].focus_set()
    
    def navigate_fields(self, current_idx, direction):
        """Navigate between fields using arrow keys"""
        keys = list(self.entries.keys())
        new_idx = (current_idx + direction) % len(keys)
        self.entries[keys[new_idx]].focus_set()
        self.entries[keys[new_idx]].select_range(0, 'end')
        return 'break'
    
    def clear_all(self):
        """Clear all input fields"""
        for entry in self.entries.values():
            entry.delete(0, 'end')
        
        for var in self.results.values():
            var.set("--")
        
        self.risk_label.config(text="RISK LEVEL: --")
        self.rec_text.delete(1.0, 'end')
        self.status.config(text="All fields cleared | Ready for new analysis")
    
    def get_numeric_value(self, entry):
        """Safely convert entry to float"""
        try:
            value = float(entry.get())
            return max(0, value)  # Ensure non-negative
        except:
            return 0.0
    
    def analyze_environment(self):
        """Comprehensive environmental analysis with GAN-inspired solutions"""
        try:
            
            values = {}
            for key, entry in self.entries.items():
                values[key] = self.get_numeric_value(entry)
            
            
            pollution_data = self.calculate_pollution(values)
            
            
            self.results["PM2.5 Concentration"].set(f"{pollution_data['pm25']:.1f} μg/m³")
            self.results["SO₂ Emissions"].set(f"{pollution_data['so2']:.2f} ppm")
            self.results["NOx Levels"].set(f"{pollution_data['nox']:.2f} ppm")
            self.results["CO Output"].set(f"{pollution_data['co']:.2f} ppm")
            
            
            aqi = self.calculate_aqi(pollution_data)
            self.results["Overall Air Quality"].set(f"{aqi} AQI")
            
            
            risk_level, risk_color = self.assess_risk(aqi, pollution_data)
            self.risk_label.config(text=f"RISK LEVEL: {risk_level}", fg=risk_color)
            
            # Generate GAN
            recommendations = self.generate_recommendations(values, pollution_data, aqi)
            self.display_recommendations(recommendations)
            
            self.status.config(text=f"Analysis Complete | AQI: {aqi} | Risk: {risk_level}")
            
        except Exception as e:
            messagebox.showerror("Analysis Error", f"Please check input values\n{str(e)}")
    
    def calculate_pollution(self, values):
        """Advanced pollution modeling"""
        
        pm25_base = 15.0
        so2_base = 8.0
        nox_base = 12.0
        co_base = 6.0
        
        
        production_factor = values['production'] / 1000
        
        
        temp = values['temperature']
        temp_factor = 1.0 + max(0, temp - 1200) * 0.001
        
        
        fuel_factor = values['fuel'] * 0.0005
        
        
        efficiency_benefit = (100 - values['efficiency']) * 0.01
        
        
        maintenance_impact = 0.7 if values['maintenance'] > 0.5 else 1.0
        
        
        exp_benefit = max(0.7, 1.0 - (values['experience'] * 0.03))
        
        # Cp
        pm25 = (pm25_base + production_factor * 10 + temp_factor * 5 + 
                fuel_factor * 3) * efficiency_benefit * maintenance_impact * exp_benefit
        
        so2 = (so2_base + fuel_factor * 8 + production_factor * 4) * maintenance_impact
        
        nox = (nox_base + temp_factor * 6 + production_factor * 5) * exp_benefit
        
        co = (co_base + fuel_factor * 6 - values['quality'] * 0.05) * maintenance_impact
        
        return {
            'pm25': max(0, pm25),
            'so2': max(0, so2),
            'nox': max(0, nox),
            'co': max(0, co)
        }
    
    def calculate_aqi(self, pollution):
        """Calculate Air Quality Index"""
        # Wa
        aqi = (pollution['pm25'] * 0.35 + 
               pollution['so2'] * 20 * 0.25 + 
               pollution['nox'] * 15 * 0.25 + 
               pollution['co'] * 10 * 0.15)
        
        return int(max(0, min(500, aqi)))
    
    def assess_risk(self, aqi, pollution):
        """Risk assessment with color coding"""
        if aqi < 50:
            return "LOW", "#27ae60"
        elif aqi < 100:
            return "MODERATE", "#f39c12"
        elif aqi < 150:
            return "UNHEALTHY", "#e67e22"
        elif aqi < 200:
            return "VERY UNHEALTHY", "#e74c3c"
        else:
            return "HAZARDOUS", "#8b0000"
    
    def generate_recommendations(self, values, pollution, aqi):
        """Generate comprehensive, creative recommendations using GAN-inspired approach"""
        recommendations = []
        
        
        recommendations.append("=" * 60)
        recommendations.append("GENERATIVE ENHANCEMENT STRATEGIES")
        recommendations.append("=" * 60)
        recommendations.append("")
        
        
        recommendations.append("🏗️  SMART GREEN INFRASTRUCTURE:")
        recommendations.append("  • Deploy AI-optimized vertical gardens on factory walls")
        recommendations.append("  • Install modular green roof systems with IoT monitoring")
        recommendations.append("  • Create micro-forest zones around perimeter using native species")
        recommendations.append("  • Implement rainwater harvesting with automated irrigation")
        recommendations.append("")
        
        
        recommendations.append("🌬️  INNOVATIVE AIR PURIFICATION:")
        recommendations.append("  • Install electrostatic precipitators with HEPA-14 filters")
        recommendations.append("  • Deploy photocatalytic oxidation units near emission sources")
        recommendations.append("  • Use bio-filtration with engineered microbial communities")
        recommendations.append("  • Implement atmospheric water generators for humidity control")
        recommendations.append("")
        
        
        if values['fuel'] > 1000:
            recommendations.append("⚡ ENERGY TRANSFORMATION PATH:")
            recommendations.append("  • Phase 1: Convert 30% to biomass gasification")
            recommendations.append("  • Phase 2: Install onsite solar micro-grid (500kW)")
            recommendations.append("  • Phase 3: Implement waste-heat recovery systems")
            recommendations.append("  • Phase 4: Deploy hydrogen fuel cell backup")
            recommendations.append("")
        
        
        recommendations.append("🔧 OPERATIONAL ENHANCEMENTS:")
        
        if values['efficiency'] < 85:
            recommendations.append("  • Upgrade to Industry 4.0 automation systems")
            recommendations.append("  • Implement predictive maintenance using ML algorithms")
            recommendations.append("  • Optimize thermal efficiency with ceramic coatings")
        
        if values['quality'] < 80:
            recommendations.append("  • Establish real-time material quality monitoring")
            recommendations.append("  • Implement closed-loop material recycling system")
            recommendations.append("  • Develop supplier sustainability scoring")
        
        if values['maintenance'] < 0.5:
            recommendations.append("  • Schedule mandatory maintenance every 3 months")
            recommendations.append("  • Create digital twin for equipment health monitoring")
        
        recommendations.append("")
        
        
        recommendations.append("🌿 ECOLOGICAL SYNERGY PROJECTS:")
        recommendations.append("  • Create pollinator habitats with native flowering plants")
        recommendations.append("  • Establish mycoremediation zones for soil detoxification")
        recommendations.append("  • Install bird/bat houses for natural pest control")
        recommendations.append("  • Develop educational eco-trail for community engagement")
        recommendations.append("")
        
        
        if pollution['co'] > 5 or aqi > 100:
            recommendations.append("♻️ CARBON MANAGEMENT SOLUTIONS:")
            recommendations.append("  • Install direct air capture units in high-emission areas")
            recommendations.append("  • Create algae photobioreactors for CO₂ sequestration")
            recommendations.append("  • Implement blockchain-based carbon credit tracking")
            recommendations.append("  • Develop circular economy partnerships")
            recommendations.append("")
        
        
        recommendations.append("👥 WORKFORCE WELLBEING PROGRAM:")
        recommendations.append("  • Establish indoor air quality monitoring in all work areas")
        recommendations.append("  • Create green break areas with living walls")
        recommendations.append("  • Implement mandatory environmental training")
        recommendations.append("  • Develop incentive programs for green innovation")
        recommendations.append("")
        
        
        recommendations.append("🤝 COMMUNITY COLLABORATION:")
        recommendations.append("  • Sponsor urban reforestation in adjacent neighborhoods")
        recommendations.append("  • Create joint air quality monitoring network")
        recommendations.append("  • Establish community garden with excess rainwater")
        recommendations.append("  • Develop transparency portal for environmental metrics")
        recommendations.append("")
        
        
        recommendations.append("📊 INTELLIGENT MONITORING SYSTEM:")
        recommendations.append("  • Deploy network of IoT air quality sensors")
        recommendations.append("  • Implement real-time emissions dashboard")
        recommendations.append("  • Use satellite imagery for environmental impact assessment")
        recommendations.append("  • Create predictive analytics for pollution forecasting")
        recommendations.append("")
        
        
        recommendations.append("🚀 LONG-TERM INNOVATION PATH:")
        recommendations.append("  • Year 1: Baseline assessment & pilot projects")
        recommendations.append("  • Year 2: Technology deployment & optimization")
        recommendations.append("  • Year 3: Scaling successful initiatives")
        recommendations.append("  • Year 5: Net-zero emissions target")
        recommendations.append("")
        
       
        recommendations.append("💰 FINANCIAL CONSIDERATIONS:")
        recommendations.append("  • Estimated ROI: 3-5 years through efficiency gains")
        recommendations.append("  • Available government incentives for green technology")
        recommendations.append("  • Potential carbon credit revenue: $50K-$200K annually")
        recommendations.append("  • Insurance premium reduction: 15-25% possible")
        recommendations.append("")
        
        
        recommendations.append("📅 RECOMMENDED IMPLEMENTATION:")
        recommendations.append("  • Immediate (1 month): Employee training & baseline audit")
        recommendations.append("  • Short-term (3 months): Quick-win green infrastructure")
        recommendations.append("  • Medium-term (12 months): Major technology deployment")
        recommendations.append("  • Long-term (24+ months): Full transformation")
        
        return recommendations
    
    def display_recommendations(self, recommendations):
        """Display recommendations in text widget"""
        self.rec_text.delete(1.0, 'end')
        
        for line in recommendations:
            
            if "=" in line:
                self.rec_text.insert('end', line + '\n', 'header')
            elif line.strip().endswith(":"):
                self.rec_text.insert('end', line + '\n', 'subheader')
            else:
                self.rec_text.insert('end', line + '\n')
        
        
        self.rec_text.tag_configure('header', font=('Segoe UI', 9, 'bold'), 
                                   foreground='#2c3e50')
        self.rec_text.tag_configure('subheader', font=('Segoe UI', 9, 'bold'),
                                   foreground='#27ae60')
    
    def export_report(self):
        """Export analysis report"""
        # Implementation for report generation
        messagebox.showinfo("Export", "Report generation feature would be implemented here.\n\nThis would include:\n- PDF generation\n- Data visualization\n- Executive summary\n- Technical specifications\n- Implementation roadmap")

def main():
    root = tk.Tk()
    
    
    try:
        root.iconbitmap('factory_icon.ico')
    except:
        pass
    
    # CW
    root.update_idletasks()
    width = 950
    height = 800
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry(f'{width}x{height}+{x}+{y}')
    
    app = AdvancedFactoryAnalyzer(root)
    
    # میانبر های صفحه کلید
    root.bind('<Control-Enter>', lambda e: app.analyze_environment())
    root.bind('<Control-e>', lambda e: app.export_report())
    root.bind('<Control-c>', lambda e: app.clear_all())
    
    root.mainloop()

if __name__ == "__main__":
    main()
