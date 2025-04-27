
import React from "react"
import { motion } from "framer-motion"

const FloatingShape = ({ className, delay, duration }) => (
  <motion.div
    className={className}
    initial={{ opacity: 0 }}
    animate={{
      opacity: [0.1, 0.3, 0.1],
      scale: [1, 1.1, 1],
      y: [0, -20, 0]
    }}
    transition={{
      duration: duration,
      repeat: Infinity,
      delay: delay,
      ease: "easeInOut"
    }}
  />
)

export default function AnimatedBackground() {
  return (
    <div className="fixed inset-0 -z-10 overflow-hidden">
      <div className="absolute inset-0 bg-gradient animate-gradient opacity-30" />
      
      <FloatingShape 
        className="absolute top-1/4 left-1/4 w-64 h-64 rounded-full bg-purple-500/10 blur-3xl"
        delay={0}
        duration={8}
      />
      <FloatingShape 
        className="absolute top-3/4 right-1/4 w-96 h-96 rounded-full bg-orange-500/10 blur-3xl"
        delay={2}
        duration={10}
      />
      <FloatingShape 
        className="absolute top-1/2 left-2/3 w-72 h-72 rounded-full bg-pink-500/10 blur-3xl"
        delay={1}
        duration={9}
      />
      
      <motion.div
        className="absolute inset-0"
        initial={{ backgroundPosition: "0 0" }}
        animate={{ backgroundPosition: "100% 100%" }}
        transition={{
          duration: 30,
          repeat: Infinity,
          repeatType: "reverse",
          ease: "linear"
        }}
        style={{
          backgroundImage: "url('data:image/svg+xml,%3Csvg width=\"100\" height=\"100\" viewBox=\"0 0 100 100\" xmlns=\"http://www.w3.org/2000/svg\"%3E%3Cpath d=\"M50 50 L50 0 A50 50 0 0 1 100 50 Z\" fill=\"rgba(147, 51, 234, 0.03)\"%3E%3C/path%3E%3C/svg%3E')",
          backgroundSize: "50px 50px"
        }}
      />
    </div>
  )
}
