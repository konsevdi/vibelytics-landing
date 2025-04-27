
import React, { useEffect, useRef } from "react"
import { motion, useScroll, useTransform } from "framer-motion"

export default function ParticleField() {
  const containerRef = useRef(null)
  const { scrollYProgress } = useScroll()
  
  const y = useTransform(scrollYProgress, [0, 1], [0, -100])
  
  return (
    <motion.div 
      ref={containerRef}
      className="fixed inset-0 pointer-events-none z-0"
      style={{ y }}
    >
      <div className="absolute inset-0">
        <div className="emotion-wave" />
        <div className="laser-beam" />
      </div>
      
      {Array.from({ length: 20 }).map((_, i) => (
        <motion.div
          key={i}
          className="particle"
          style={{
            left: `${Math.random() * 100}%`,
            top: `${Math.random() * 100}%`,
            width: `${Math.random() * 3 + 1}px`,
            height: `${Math.random() * 3 + 1}px`,
            background: `rgba(${147 + Math.random() * 50}, ${51 + Math.random() * 50}, ${234 + Math.random() * 20}, ${0.3 + Math.random() * 0.4})`
          }}
          animate={{
            y: [0, -30, 0],
            opacity: [0.2, 0.5, 0.2]
          }}
          transition={{
            duration: 3 + Math.random() * 2,
            repeat: Infinity,
            delay: Math.random() * 2
          }}
        />
      ))}
    </motion.div>
  )
}
