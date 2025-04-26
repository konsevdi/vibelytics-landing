
import { createClient } from '@supabase/supabase-js'

const supabaseUrl = 'https://nwxjvaayxsizcqseefgr.supabase.co'
const supabaseAnonKey = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im53eGp2YWF5eHNpemNxc2VlZmdyIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDUwOTQ4MzQsImV4cCI6MjA2MDY3MDgzNH0.J3KLrDPazt1-3Oz9pnGRLTp7JSHv5NYQznJF4IICNqQ'

export const supabase = createClient(supabaseUrl, supabaseAnonKey)
